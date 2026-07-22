"""
File validation module.
"""

from pathlib import Path

from src.logger import get_logger

logger = get_logger()


def validate_file(file_path: Path) -> None:
    """
    Validate that the source file exists.

    Args:
        file_path (Path): Path to the source file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """

    logger.info(f"Validating source file: {file_path}")

    if not file_path.exists():
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    logger.info("Source file validation passed.")