import pandas as pd
from logger import get_logger

logger = get_logger()


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply business transformations.
    """

    logger.info("Starting data transformation")

    # Remove leading/trailing spaces
    df["name"] = df["name"].str.strip()

    # Department uppercase
    df["department"] = df["department"].str.upper()

    logger.info("Transformation completed")

    return df