"""
Test schema validator.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.validations.schema_validator import validate_schema


def test_schema_validator():
    df = extract_csv(DATASET_DIR / "employees.csv")

    validate_schema(df)

    print("✅ Schema validator test passed.")


if __name__ == "__main__":
    test_schema_validator()
