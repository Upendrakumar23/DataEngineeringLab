"""
Test blank validator.
"""

import pytest

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.blank_validator import validate_blanks


def test_blank_validator():
    """Test blank validator with clean data."""

    df = extract_csv(DATASET_DIR / "employees.csv")

    validate_blanks(df)


def test_blank_validator_negative():
    """Test blank validator with blank values."""

    df = extract_csv(DATASET_DIR / "test" / "employees_blank.csv")

    with pytest.raises(ValueError):
        validate_blanks(df)
