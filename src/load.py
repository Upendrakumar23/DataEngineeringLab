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
        """

        inserted_rows = 0

        for _, row in df.iterrows():
            cursor.execute(
                insert_query,
                (
                    row["employee_code"],
                    row["name"],
                    row["department"],
                    row["salary"],
                ),
            )

            inserted_rows += 1

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