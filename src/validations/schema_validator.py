"""
Schema validation module.
"""

import pandas as pd

from src.config import REQUIRED_COLUMNS
from src.logger import get_logger

logger = get_logger()


def validate_schema(df: pd.DataFrame) -> None:
    """
    Validate that the DataFrame contains all required columns.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Raises:
        ValueError: If one or more required columns are missing.
    """

    logger.info("Validating DataFrame schema...")

    missing_columns = [
        column for column in REQUIRED_COLUMNS if column not in df.columns
    ]

    if missing_columns:
        logger.error(f"Missing required columns: {missing_columns}")
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    logger.info("Schema validation passed.")
