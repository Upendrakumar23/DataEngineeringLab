# Day 9 – Production Quality, Testing & Code Coverage

**Project:** DataEngineeringLab
**Module:** Python ETL Pipeline
**Status:** ✅ Completed

---

# Objective

Today's goal was to transform the ETL project from a working application into a **production-quality Python project** by introducing:

- Code formatting
- Linting
- Unit Testing
- Integration Testing
- Test Coverage
- Repository cleanup
- Production project structure

---

# Learning Outcomes

By the end of Day 9, I learned:

- Importance of code quality in professional software development
- Difference between formatting, linting and testing
- How to measure code coverage
- How to write unit tests using mocks
- Difference between unit tests and integration tests
- How to improve repository structure
- Production coding standards

---

# Module 1 – Code Quality

## Why Code Quality Matters

A project is not considered production-ready simply because it works.

Professional projects must be:

- Readable
- Maintainable
- Consistent
- Testable
- Easy for other developers to understand

---

## Tools Used

### Black

Purpose:

- Automatically formats Python code
- Enforces PEP-8 formatting

Command

```bash
black .
```

---

### isort

Purpose:

- Automatically sorts imports

Command

```bash
isort .
```

---

### flake8

Purpose:

- Static code analysis
- Detects

- unused imports
- unused variables
- incorrect spacing
- long lines
- style violations

Command

```bash
flake8 .
```

---

## Configuration Files

### pyproject.toml

Used by

- Black
- isort

Example

```toml
[tool.black]
line-length = 88
target-version = ["py38"]

[tool.isort]
profile = "black"
line_length = 88
```

---

### .flake8

```ini
[flake8]
max-line-length = 88
exclude =
    .git,
    __pycache__,
    venv
```

---

### .coveragerc

```ini
[run]
source = src

omit =
    tests/*
    venv/*
    src/archive/*
```

---

# Module 2 – Fixing Lint Issues

The project initially contained several flake8 errors.

Examples:

- Unused imports
- Unused variables
- Duplicate imports
- Import order
- Blank line violations

After fixing all issues

```bash
flake8 .
```

produced

```
(no output)
```

which indicates

✅ Zero lint errors

---

# Module 3 – Test Coverage

## What is Code Coverage?

Coverage tells us

> How much of our code executes while running tests.

It **does NOT** tell us whether the tests are good.

---

## Coverage Command

```bash
pytest --cov=src --cov-report=term-missing
```

---

# Module 4 – Unit Testing main.py

Previously

```
main.py

Coverage = 0%
```

Reason:

No unit test existed for the ETL entry point.

---

## New Test

Created

```
tests/unit/test_main.py
```

Two tests were added

### Success Flow

Verifies

- validate_file()
- extract_csv()
- validate_data()
- transform_data()
- load_data()

are executed correctly.

---

### Failure Flow

Verifies

- exceptions are logged
- exceptions are re-raised

---

## Mocking

Used

```python
unittest.mock.patch
```

instead of

- real database
- real CSV
- real ETL execution

This makes tests

- faster
- isolated
- deterministic

---

# Module 5 – Integration Testing

Integration tests execute the entire ETL pipeline.

They verify

CSV

↓

Validation

↓

Transformation

↓

Incremental UPSERT

↓

PostgreSQL

---

Initially

Tests failed because

Docker PostgreSQL container was not running.

Error

```
connection refused
```

Root cause

```
Infrastructure issue

NOT

Application issue
```

After starting PostgreSQL

All integration tests passed.

---

# Module 6 – Final Test Results

```
25 Passed

0 Failed

0 Skipped
```

Execution time

```
16.40 seconds
```

---

# Module 7 – Coverage Report

Final Coverage

| Module                 | Coverage |
| ---------------------- | -------: |
| config.py              |      94% |
| database.py            |     100% |
| extract.py             |      75% |
| load_incremental.py    |     100% |
| logger.py              |     100% |
| main.py                |      98% |
| transform.py           |      79% |
| blank_validator.py     |     100% |
| duplicate_validator.py |     100% |
| file_validator.py      |     100% |
| null_validator.py      |     100% |
| salary_validator.py    |      80% |
| schema_validator.py    |      82% |
| validator.py           |     100% |

Overall

```
83%
```

---

# Why Overall Coverage Isn't 100%

Coverage is reduced because

Archived learning modules

```
load_batch.py
```

are not part of the active application.

Rather than writing meaningless tests,

we excluded archived code from coverage.

---

# Module 8 – Repository Refactoring

Old structure

```
src/

load_batch.py
load_simple.py
load_incremental.py
```

New structure

```
src/

archive/
    load_batch.py
    load_simple.py

load_incremental.py
```

Benefits

- Cleaner repository
- Easier maintenance
- Clear production implementation

---

# Unit Test vs Integration Test

## Unit Test

Tests

One function

Uses

Mocks

Fast

No database

---

## Integration Test

Tests

Entire ETL pipeline

Uses

Real PostgreSQL

Real CSV

Real UPSERT

Slower

Higher confidence

---

# Important Lessons

## Black

Formats code

---

## isort

Sorts imports

---

## flake8

Checks code quality

---

## pytest

Runs tests

---

## pytest-cov

Measures code coverage

---

## unittest.mock

Allows testing code without

- files
- databases
- APIs

---

# Professional Software Development Flow

```
Write Code

↓

Run Black

↓

Run isort

↓

Run flake8

↓

Run pytest

↓

Check Coverage

↓

Commit

↓

Push to GitHub

↓

GitHub Actions

↓

Deploy
```

---

# Best Practices Learned

✅ Modular project structure

✅ Logging instead of print()

✅ Environment configuration

✅ Transaction handling

✅ Incremental UPSERT

✅ Unit testing

✅ Integration testing

✅ Mocking

✅ Code formatting

✅ Static analysis

✅ Coverage measurement

---

# Commands Learned

Format

```bash
black .
```

Sort Imports

```bash
isort .
```

Lint

```bash
flake8 .
```

Run Tests

```bash
pytest
```

Run Coverage

```bash
pytest --cov=src --cov-report=term-missing
```

Generate HTML Report

```bash
pytest --cov=src --cov-report=html
```

---

# Final Project Status

| Category            | Status |
| ------------------- | ------ |
| Docker              | ✅      |
| PostgreSQL          | ✅      |
| Python ETL          | ✅      |
| Incremental UPSERT  | ✅      |
| Logging             | ✅      |
| Validation          | ✅      |
| Transactions        | ✅      |
| Unit Testing        | ✅      |
| Integration Testing | ✅      |
| Code Quality        | ✅      |
| Coverage            | ✅      |

---

# Day 9 Summary

Today the ETL project evolved from a functional prototype into a **production-quality Python application**.

Key achievements included introducing professional code quality tools (Black, isort, and flake8), adding comprehensive unit and integration tests, measuring code coverage, refactoring the repository structure, and improving the main ETL entry point through mock-based testing.

By the end of the day, the project reached:

- **25 Passing Tests**
- **0 Test Failures**
- **83% Code Coverage**
- **Production-ready Project Structure**
- **PEP-8 Compliant Code**
- **Professional Testing Framework**

This project is now suitable for inclusion in a GitHub portfolio and provides a strong foundation for discussing ETL design, testing strategies, and Python engineering practices during Data Engineering interviews.

---

# Tomorrow (Day 10)

## CI/CD with GitHub Actions

Topics

- GitHub Actions
- Automated Testing
- CI Pipeline
- Repository Badges
- Professional README
- Architecture Diagram
- Portfolio Review

Goal

> Transform the repository into a professional, interview-ready open-source project.
