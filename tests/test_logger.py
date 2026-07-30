"""
Test logger configuration.
"""

from src.logger import get_logger


def test_logger():
    logger = get_logger()

    assert logger.name == "etl_logger"
    assert logger.handlers

    logger.info("ETL Started")
    logger.info("CSV Loaded Successfully")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")

    print("✅ Logger test passed.")


if __name__ == "__main__":
    test_logger()
