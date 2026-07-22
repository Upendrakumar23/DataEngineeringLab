from src.config import DATASET_DIR
from src.validations.file_validator import validate_file


def test_file_validator():
    file_path = DATASET_DIR / "employees.csv"

    validate_file(file_path)

    print("✅ File validator test passed.")


if __name__ == "__main__":
    test_file_validator()