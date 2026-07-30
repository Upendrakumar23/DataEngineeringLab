"""
Main ETL pipeline.
"""

from datetime import datetime

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.load_incremental import load_data
from src.logger import get_logger
from src.transform import transform_data
from src.validations.file_validator import validate_file
from src.validations.validator import validate_data

logger = get_logger()


def main():
    start_time = datetime.now()

    try:
        file_path = DATASET_DIR / "employees.csv"

        logger.info("Starting ETL Pipeline")

        # Step 1: Validate source file
        validate_file(file_path)

        # Step 2: Extract
        df = extract_csv(file_path)
        rows_extracted = len(df)

        # Step 3: Validate data
        validate_data(df)
        rows_validated = len(df)

        # Step 4: Transform
        df = transform_data(df)
        rows_transformed = len(df)

        # Step 5: Load
        rows_loaded = load_data(df)

        end_time = datetime.now()
        duration = end_time - start_time

        logger.info("=" * 70)
        logger.info("ETL EXECUTION SUMMARY")
        logger.info("=" * 70)
        logger.info("Pipeline Name    : Employee ETL")
        logger.info("Source File      : %s", file_path.name)
        logger.info("Load Strategy    : Incremental UPSERT")
        logger.info("Rows Extracted   : %d", rows_extracted)
        logger.info("Rows Validated   : %d", rows_validated)
        logger.info("Rows Transformed : %d", rows_transformed)
        logger.info("Rows Processed   : %d", rows_loaded)
        logger.info("Start Time       : %s", start_time.strftime("%Y-%m-%d %H:%M:%S"))
        logger.info("End Time         : %s", end_time.strftime("%Y-%m-%d %H:%M:%S"))
        logger.info("Duration         : %.2f seconds", duration.total_seconds())
        logger.info("Status           : SUCCESS")
        logger.info("=" * 70)

        logger.info("ETL Pipeline completed successfully.")

    except Exception:
        logger.exception("ETL Pipeline failed.")
        raise


if __name__ == "__main__":
    main()
