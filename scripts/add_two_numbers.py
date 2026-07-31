"""
Script to add two numbers.

Usage:
    python scripts/add_two_numbers.py <num1> <num2>

Example:
    python scripts/add_two_numbers.py 5 3
    Output: 8
"""

import sys


def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def main():
    if len(sys.argv) != 3:
        print("Usage: python add_two_numbers.py <num1> <num2>")
        print("Example: python add_two_numbers.py 5 3")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Error: Both arguments must be valid numbers.")
        sys.exit(1)

    result = add_numbers(num1, num2)
    print(f"{num1} + {num2} = {result}")


if __name__ == "__main__":
    main()
