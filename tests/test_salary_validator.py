"""
Test salary validator.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.salary_validator import validate_salary


def test_salary_validator():
    df = extract_csv(DATASET_DIR / "employees.csv")

    validate_salary(df)

    print("✅ Salary validator test passed.")


if __name__ == "__main__":
    test_salary_validator()