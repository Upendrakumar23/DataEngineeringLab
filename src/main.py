"""
Main ETL pipeline.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.load import load_data
from src.logger import get_logger
from src.transform import transform_data
from src.validations.file_validator import validate_file
from src.validations.validator import validate_data

logger = get_logger()


def main():
    try:
        file_path = DATASET_DIR / "employees.csv"

        logger.info("Starting ETL Pipeline")

        # Step 1: Validate source file
        validate_file(file_path)

        # Step 2: Extract
        df = extract_csv(file_path)

        # Step 3: Validate data
        validate_data(df)

        # Step 4: Transform
        df = transform_data(df)

        # Step 5: Load
        load_data(df)

        logger.info("ETL Pipeline completed successfully.")

    except Exception:
        logger.exception("ETL Pipeline failed.")
        raise


if __name__ == "__main__":
    main()