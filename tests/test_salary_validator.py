"""
Test salary validator - positive and negative cases.
"""

import pytest

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.salary_validator import validate_salary


def test_salary_validator():
    """Test salary validator with clean data (valid salaries)."""
    df = extract_csv(DATASET_DIR / "employees.csv")

    validate_salary(df)


def test_salary_validator_negative():
    """Test salary validator with invalid salary values."""
    df = extract_csv(DATASET_DIR / "test" / "employees_invalid_salary.csv")

    with pytest.raises(ValueError):
        validate_salary(df)
