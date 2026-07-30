"""
Duplicate value validation module.
"""

import pandas as pd

from src.logger import get_logger

logger = get_logger()

UNIQUE_COLUMNS = [
    "employee_code",
]


def validate_duplicates(df: pd.DataFrame) -> None:
    """
    Validate that unique columns do not contain duplicate values.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Raises:
        ValueError: If duplicate values are found.
    """

    logger.info("Validating duplicate records...")

    duplicate_summary = {}

    for column in UNIQUE_COLUMNS:
        duplicate_count = df[column].duplicated().sum()

        if duplicate_count > 0:
            duplicate_summary[column] = duplicate_count

    if duplicate_summary:
        error_message = ", ".join(
            f"{column}: {count}" for column, count in duplicate_summary.items()
        )

        logger.error(f"Duplicate values found -> {error_message}")
        raise ValueError(f"Duplicate values found -> {error_message}")

    logger.info("Duplicate validation passed.")
