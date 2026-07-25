"""
Test null validator - positive and negative cases.
"""

import pytest

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.null_validator import validate_nulls


def test_null_validator():
    """Test null validator with clean data (no nulls)."""
    df = extract_csv(DATASET_DIR / "employees.csv")

    validate_nulls(df)


def test_null_validator_negative():
    """Test null validator with data containing null values."""
    df = extract_csv(DATASET_DIR / "test" / "employees_null.csv")

    with pytest.raises(ValueError):
        validate_nulls(df)
