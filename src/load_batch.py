from psycopg import DatabaseError

from src.database import get_connection
from src.logger import get_logger

logger = get_logger()


def load_data(df, batch_size=1000):
    """Load data into PostgreSQL using batch INSERT."""

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

        data = [
            (
                row["employee_code"],
                row["name"],
                row["department"],
                row["salary"],
            )
            for _, row in df.iterrows()
        ]

        logger.info("Starting batch data load...")

        processed = 0
        batch_count = 0

        for i in range(0, len(data), batch_size):
            batch = data[i : i + batch_size]

            cursor.executemany(insert_query, batch)

            processed += len(batch)
            batch_count += 1

        conn.commit()

        logger.info("=" * 60)
        logger.info("ETL Load Summary")
        logger.info("Load Strategy  : Batch INSERT")
        logger.info("Rows Processed : %d", processed)
        logger.info("Batch Size     : %d", batch_size)
        logger.info("Batches        : %d", batch_count)
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
