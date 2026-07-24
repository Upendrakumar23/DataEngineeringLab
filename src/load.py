"""
Load data into PostgreSQL.
"""

from psycopg import DatabaseError

from src.database import get_connection
from src.logger import get_logger

logger = get_logger()


def load_data(df) -> None:
    """
    Load employee data into PostgreSQL.

    Args:
        df: Transformed DataFrame.
    """

    logger.info("Starting data load.")

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO employees (
            employee_code,
            name,
            department,
            salary
            )
        VALUES (%s, %s, %s, %s)

        ON CONFLICT (employee_code)
        DO UPDATE SET
        name = EXCLUDED.name,
        department = EXCLUDED.department,
        salary = EXCLUDED.salary;
        """

        data = [
    (
        row["employee_code"],
        row["name"],
        row["department"],
        row["salary"],
    )
    for _, row in df.iterrows()
]

        batch_size = 1000

        inserted_rows = 0

        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]

        cursor.executemany(insert_query, batch)

        inserted_rows += len(batch)

        inserted_rows = len(data)

        conn.commit()

        logger.info(
            f"Successfully loaded {inserted_rows} records into employees table."
        )

    except DatabaseError:
        if conn:
            conn.rollback()

        logger.exception("Database transaction rolled back.")
        raise

    except Exception:
        if conn:
            conn.rollback()

        logger.exception("Unexpected error while loading data.")
        raise

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

        logger.info("Database connection closed.")
