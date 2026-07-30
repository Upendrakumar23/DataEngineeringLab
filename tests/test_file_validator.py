"""
Test file validator - positive and negative cases.
"""

from pathlib import Path

import pytest

from src.config import DATASET_DIR
from src.validations.file_validator import validate_file


def test_file_validator():
    """Test file validator with an existing file."""
    file_path = DATASET_DIR / "employees.csv"

    validate_file(file_path)


def test_missing_file():
    """Test file validator with a missing file."""
    with pytest.raises(FileNotFoundError):
        validate_file(Path("datasets/not_exists.csv"))
