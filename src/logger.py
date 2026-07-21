import logging
import os

import config


def get_logger():
    """
    Configure and return a logger instance.
    """

    # Create logs directory if it doesn't exist
    os.makedirs(config.LOG_DIR, exist_ok=True)

    log_file = os.path.join(config.LOG_DIR, "etl.log")

    logger = logging.getLogger("etl_logger")

    # Avoid adding duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(getattr(logging, config.LOG_LEVEL.upper(), logging.INFO))

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s"
    )

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger