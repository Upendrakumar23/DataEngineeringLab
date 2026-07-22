"""
Test data transformation.
"""

from src.config import DATASET_DIR
from src.extract import extract_csv
from src.transform import transform_data


def test_transform():
    # Extract
    df = extract_csv(DATASET_DIR / "employees.csv")

    print("\nBefore Transformation:")
    print(df)

    # Transform
    transformed_df = transform_data(df)

    print("\nAfter Transformation:")
    print(transformed_df)

    # Basic Assertions
    assert len(df) == len(transformed_df)

    print("\n✅ Transform test passed.")


if __name__ == "__main__":
    test_transform()