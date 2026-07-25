"""
Test duplicate validator - positive and negative cases.
"""

import pytest

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.duplicate_validator import validate_duplicates


def test_duplicate_validator():
    """Test duplicate validator with clean data (no duplicates)."""
    df = extract_csv(DATASET_DIR / "employees.csv")

    validate_duplicates(df)


def test_duplicate_validator_negative():
    """Test duplicate validator with data containing duplicates."""
    df = extract_csv(
        DATASET_DIR / "test" / "employees_duplicate.csv"
    )

    with pytest.raises(ValueError):
        validate_duplicates(df)

