"""
Blank value validation module.
"""

import pandas as pd

from src.logger import get_logger

logger = get_logger()


def validate_blanks(df: pd.DataFrame) -> None:
    """
    Validate that required text columns do not contain blank values.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Raises:
        ValueError: If blank values are found.
    """

    logger.info("Validating blank values...")

    # Only validate text columns
    text_columns = [
        "employee_code",
        "name",
        "department",
    ]

    blank_summary = {}

    for column in text_columns:
        blank_count = df[column].astype(str).str.strip().eq("").sum()

        if blank_count > 0:
            blank_summary[column] = blank_count

    if blank_summary:
        error_message = ", ".join(
            f"{column}: {count}" for column, count in blank_summary.items()
        )

        logger.error(f"Blank values found -> {error_message}")
        raise ValueError(f"Blank values found -> {error_message}")

    logger.info("Blank validation passed.")
