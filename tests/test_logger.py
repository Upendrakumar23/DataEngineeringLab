from logger import get_logger

logger = get_logger()

logger.info("ETL Started")
logger.info("CSV Loaded")
logger.warning("This is a warning")
logger.error("This is an error")