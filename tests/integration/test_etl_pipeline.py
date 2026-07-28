"""
Integration tests for the complete ETL pipeline.
"""


import pytest
from psycopg import DatabaseError
from src.config import DATASET_DIR
from src.database import get_connection
from src.extract import extract_csv
from src.load_incremental import load_data
from src.transform import transform_data
from src.validations.file_validator import validate_file
from src.validations.validator import validate_data


def clear_table():
    """
    Remove all records from the employees table before each test.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("TRUNCATE TABLE employees;")

    conn.commit()

    cursor.close()
    conn.close()


def run_etl(file_path):
    """
    Execute the complete ETL pipeline and return the transformed
    DataFrame along with the number of processed rows.
    """
    validate_file(file_path)

    df = extract_csv(file_path)

    validate_data(df)

    df = transform_data(df)

    rows = load_data(df)

    return df, rows


def test_complete_etl_pipeline():
    """
    Verify that the complete ETL pipeline loads all records
    into the database successfully.
    """

    clear_table()

    file_path = DATASET_DIR / "employees.csv"

    df, rows = run_etl(file_path)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM employees;")

    count = cursor.fetchone()[0]

    assert rows == len(df)
    assert count == len(df)

    cursor.close()
    conn.close()


def test_incremental_loading():
    """
    Verify that running the ETL pipeline multiple times
    does not create duplicate records.
    """

    clear_table()

    file_path = DATASET_DIR / "employees.csv"

    df, _ = run_etl(file_path)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM employees;")

    first_count = cursor.fetchone()[0]

    assert first_count == len(df)

    # Run the ETL pipeline again
    run_etl(file_path)

    cursor.execute("SELECT COUNT(*) FROM employees;")

    second_count = cursor.fetchone()[0]

    assert second_count == len(df)

    cursor.close()
    conn.close()


def test_upsert_updates_existing_record():
    """
    Verify that UPSERT updates an existing employee instead of inserting
    a duplicate record.
    """

    clear_table()

    file_path = DATASET_DIR / "employees.csv"

    df, _ = run_etl(file_path)

    # Change salary of EMP003
    df.loc[df["employee_code"] == "EMP003", "salary"] = 90000

    # Run load again (UPSERT)
    load_data(df)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT salary
        FROM employees
        WHERE employee_code = 'EMP003';
        """
    )

    salary = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM employees;
        """
    )

    count = cursor.fetchone()[0]

    assert salary == 90000

    assert count == len(df)

    cursor.close()
    conn.close()


def test_transaction_rollback():
    """
    Verify that the entire transaction is rolled back
    when a database error occurs.
    """

    clear_table()

    file_path = DATASET_DIR / "employees.csv"

    df, _ = run_etl(file_path)

    # Introduce invalid data to trigger a database error
    df.loc[df["employee_code"] == "EMP003", "salary"] = "INVALID"

    with pytest.raises(DatabaseError):
        load_data(df)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM employees;")

    count = cursor.fetchone()[0]

    # Database should still contain only the rows from the
    # successful initial load.
    assert count == len(df)

    cursor.close()
    conn.close()
