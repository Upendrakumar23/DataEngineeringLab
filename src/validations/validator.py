"""
Master validation module.
"""

import pandas as pd

from src.logger import get_logger
from src.validations.blank_validator import validate_blanks
from src.validations.duplicate_validator import validate_duplicates
from src.validations.null_validator import validate_nulls
from src.validations.salary_validator import validate_salary
from src.validations.schema_validator import validate_schema

logger = get_logger()


def validate_data(df: pd.DataFrame) -> None:
    """
    Execute all DataFrame validation checks.
    """

    logger.info("=" * 60)
    logger.info("Starting Data Validation")

    validate_schema(df)
    validate_nulls(df)
    validate_blanks(df)
    validate_duplicates(df)
    validate_salary(df)

    logger.info("All data validations passed successfully.")
    logger.info("=" * 60)
