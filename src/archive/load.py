"""
Load data into PostgreSQL using batch UPSERT.

This module provides functionality to load transformed employee data
into the PostgreSQL database using batch operations with conflict
resolution (UPSERT).
"""

from typing import List, Tuple

import pandas as pd
from psycopg import DatabaseError

from src.database import get_connection
from src.logger import get_logger

logger = get_logger()


def load_data(df: pd.DataFrame, batch_size: int = 1000) -> int:
    """
    Load employee data into PostgreSQL using batch UPSERT.

    Args:
        df: Transformed DataFrame containing employee records with
            columns: employee_code, name, department, salary.
        batch_size: Number of records to process per batch.
            Defaults to 1000.

    Returns:
        Total number of rows processed.

    Raises:
        DatabaseError: If a database operation fails.
        Exception: If an unexpected error occurs during loading.
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

        data: List[Tuple[str, str, str, float]] = [
            (
                row["employee_code"],
                row["name"],
                row["department"],
                row["salary"],
            )
            for _, row in df.iterrows()
        ]

        logger.info("Starting data load...")

        processed = 0
        batch_count = 0

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

        conn.commit()

        logger.info("=" * 60)
        logger.info("ETL Load Summary")
        logger.info("=" * 60)
        logger.info("Load Strategy  : Batch UPSERT")
        logger.info("Rows Processed : %d", processed)
        logger.info("Batch Size     : %d", batch_size)
        logger.info("Batches        : %d", batch_count)
        logger.info("Target Table   : employees")
        logger.info("Status         : SUCCESS")
        logger.info("=" * 60)

        return processed

    except DatabaseError:
        if conn:
            logger.error("Database error detected. Rolling back transaction...")
            conn.rollback()

        logger.exception("Database transaction rolled back.")
        raise

    except Exception:
        if conn:
            logger.error("Unexpected error detected. Rolling back transaction...")
            conn.rollback()

        logger.exception("Unexpected error while loading data.")
        raise

    finally:
        if conn:
            conn.close()
            logger.info("Database connection closed.")
