from psycopg import DatabaseError

from src.database import get_connection
from src.logger import get_logger

logger = get_logger()


def load_data(df):
    """Load data into PostgreSQL using row-by-row INSERT."""

    conn = None

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
            VALUES (%s, %s, %s, %s);
        """

        inserted_rows = 0

        logger.info("Starting data load...")

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

        logger.info("=" * 60)
        logger.info("ETL Load Summary")
        logger.info("Load Strategy  : Simple INSERT")
        logger.info("Rows Processed : %d", inserted_rows)
        logger.info("Target Table   : employees")
        logger.info("Status         : SUCCESS")
        logger.info("=" * 60)

    except DatabaseError as e:
        if conn:
            conn.rollback()
        logger.exception("Database error: %s", e)
        raise

    finally:
        if conn:
            conn.close()
            logger.info("Database connection closed.")
