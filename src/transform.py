"""
Data transformation module.
"""

import pandas as pd

from src.logger import get_logger

logger = get_logger()


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply business transformations.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Transformed DataFrame.
    """

    logger.info("Starting data transformation.")

    try:
        # Work on a copy to avoid modifying the original DataFrame
        transformed_df = df.copy()

        # Remove leading/trailing spaces
        transformed_df["name"] = transformed_df["name"].str.strip()

        # Convert department names to uppercase
        transformed_df["department"] = transformed_df["department"].str.upper()

        logger.info("Data transformation completed successfully.")

        return transformed_df

    except Exception:
        logger.exception("Data transformation failed.")
        raise
