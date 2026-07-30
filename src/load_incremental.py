"""
Load data into PostgreSQL using Incremental UPSERT.
"""

from psycopg import DatabaseError

from src.database import get_connection
from src.logger import get_logger

logger = get_logger()


def load_data(df, batch_size=1000):
    """
    Load data into PostgreSQL using batch UPSERT.

    Args:
        df (pandas.DataFrame): Transformed employee data.
        batch_size (int): Number of records to process per batch.

    Returns:
        int: Total number of rows processed.
    """

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        upsert_query = """
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

        # Convert DataFrame into list of tuples
        data = [
            (
                row["employee_code"],
                row["name"],
                row["department"],
                row["salary"],
            )
            for _, row in df.iterrows()
        ]

        logger.info("Starting incremental data load...")

        processed = 0
        batch_count = 0

        # Batch processing
        for i in range(0, len(data), batch_size):
            batch = data[i : i + batch_size]

            cursor.executemany(upsert_query, batch)

            processed += len(batch)
            batch_count += 1

            logger.info(
                "Batch %d completed (%d records).",
                batch_count,
                len(batch),
            )

        # Commit transaction
        conn.commit()

        logger.info("=" * 60)
        logger.info("ETL Load Summary")
        logger.info("=" * 60)
        logger.info("Load Strategy  : Incremental UPSERT")
        logger.info("Rows Processed : %d", processed)
        logger.info("Batch Size     : %d", batch_size)
        logger.info("Batches        : %d", batch_count)
        logger.info("Target Table   : employees")
        logger.info("Status         : SUCCESS")
        logger.info("=" * 60)

        return processed

    except DatabaseError as e:
        if conn:
            logger.error("Database error detected. Rolling back transaction...")
            conn.rollback()

        logger.exception("Database error: %s", e)
        raise

    except Exception as e:
        if conn:
            logger.error("Unexpected error detected. Rolling back transaction...")
            conn.rollback()

        logger.exception("Unexpected error: %s", e)
        raise

    finally:
        if conn:
            conn.close()
            logger.info("Database connection closed.")
