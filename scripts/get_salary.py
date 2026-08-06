"""
Look up an employee's salary by employee code.

Usage:
    python scripts/get_salary.py EMP001
"""

import csv
import sys
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "datasets" / "employees.csv"


def get_salary(employee_code: str) -> str | None:
    """Return the salary for the given employee code, or None if not found."""
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["employee_code"].strip().lower() == employee_code.strip().lower():
                return row["salary"].strip()
    return None


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python get_salary.py <employee_code>")
        print("Example: python get_salary.py EMP001")
        sys.exit(1)

    employee_code = sys.argv[1]
    salary = get_salary(employee_code)

    if salary is None:
        print(f"Employee code '{employee_code}' not found in {CSV_PATH.name} file.")
        sys.exit(1)

    print(f"Salary for {employee_code}: {salary}")


if __name__ == "__main__":
    main()
