"""
Salary validation module.
"""

import pandas as pd

from src.logger import get_logger

logger = get_logger()


def validate_salary(df: pd.DataFrame) -> None:
    """
    Validate salary values.

    Rules:
    - Salary must be numeric.
    - Salary must be greater than zero.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Raises:
        ValueError: If invalid salary values are found.
    """

    logger.info("Validating salary values...")

    # Convert salary to numeric
    salary = pd.to_numeric(df["salary"], errors="coerce")

    # Check non-numeric values
    if salary.isnull().any():
        logger.error("Non-numeric salary values found.")
        raise ValueError("Salary column contains non-numeric values.")

    # Check zero or negative salary
    invalid_salary = salary <= 0

    if invalid_salary.any():
        count = invalid_salary.sum()

        logger.error(f"Invalid salary values found. Records: {count}")

        raise ValueError(f"Salary must be greater than zero. Invalid records: {count}")

    logger.info("Salary validation passed.")
