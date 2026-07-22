"""
Test salary validator with invalid salary values.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.salary_validator import validate_salary


def test_salary_validator_negative():
    df = extract_csv(
        DATASET_DIR / "test" / "employees_invalid_salary.csv"
    )

    try:
        validate_salary(df)
    except ValueError:
        print("✅ Salary validation test passed.")
    else:
        raise AssertionError("Expected ValueError was not raised.")


if __name__ == "__main__":
    test_salary_validator_negative()