"""
Null value validation module.
"""

import pandas as pd

from src.config import REQUIRED_COLUMNS
from src.logger import get_logger

logger = get_logger()


def validate_nulls(df: pd.DataFrame) -> None:
    """
    Validate that required columns do not contain null values.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Raises:
        ValueError: If null values are found in required columns.
    """

    logger.info("Validating null values...")

    null_counts = df[REQUIRED_COLUMNS].isnull().sum()
    invalid_columns = null_counts[null_counts > 0]

    if not invalid_columns.empty:
        error_message = ", ".join(
            f"{column}: {count}" for column, count in invalid_columns.items()
        )

        logger.error(f"Null values found -> {error_message}")
        raise ValueError(f"Null values found -> {error_message}")

    logger.info("Null validation passed.")
