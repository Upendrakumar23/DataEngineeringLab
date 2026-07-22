"""
Extract data from source files.
"""

import pandas as pd

from src.logger import get_logger

logger = get_logger()


def extract_csv(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Extracted data.

    Raises:
        Exception: If the CSV cannot be read.
    """

    logger.info(f"Reading CSV file: {file_path}")

    try:
        df = pd.read_csv(file_path)

        logger.info(
            f"CSV loaded successfully. Records found: {len(df)}"
        )

        return df

    except Exception as e:
        logger.exception(f"Failed to read CSV file: {file_path}")
        raise