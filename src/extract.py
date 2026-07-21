import pandas as pd
from logger import get_logger

logger = get_logger()


def extract_csv(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file.

    Args:
        file_path: Path to CSV file

    Returns:
        Pandas DataFrame
    """
    logger.info(f"Reading CSV file: {file_path}")

    df = pd.read_csv(file_path)

    logger.info(f"Successfully loaded {len(df)} records")

    return df