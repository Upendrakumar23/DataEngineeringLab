import logging
import os

from src.config import LOG_DIR, LOG_LEVEL


def get_logger():
    """
    Configure and return a singleton logger instance.
    """

    logger = logging.getLogger("etl_logger")

    if logger.handlers:
        return logger

    os.makedirs(LOG_DIR, exist_ok=True)

    log_file = os.path.join(LOG_DIR, "etl.log")

    logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

    formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s")

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
