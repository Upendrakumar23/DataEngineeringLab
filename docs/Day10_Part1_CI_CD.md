# Day 10 – Part 1
# Production CI/CD Pipeline using GitHub Actions

**Project:** DataEngineeringLab

**Date:** 30 July 2026

---

# Objective

Transform the ETL project into a production-ready repository by implementing Continuous Integration (CI) using GitHub Actions.

The pipeline automatically validates code quality, provisions a PostgreSQL database, executes tests, and generates coverage reports on every push and pull request.

---

# Learning Objectives

By the end of this session, I learned how to:

- Implement GitHub Actions
- Configure Continuous Integration (CI)
- Automate code quality checks
- Provision PostgreSQL inside GitHub Actions
- Execute Unit and Integration Tests automatically
- Generate Code Coverage reports
- Upload build artifacts
- Debug CI failures
- Build a production-style pipeline

---

# Topics Covered

## 1. GitHub Actions

Created GitHub workflow:

```text
.github/
└── workflows/
    └── python-ci.yml
```

Workflow triggers:

- Push
- Pull Request

Supported branches:

- main
- master

---

## 2. Python Environment

Configured GitHub runner with

- Ubuntu Latest
- Python 3.8

Installed project dependencies using

```bash
pip install -r requirements.txt
```

---

## 3. PostgreSQL Service

Provisioned PostgreSQL automatically inside GitHub Actions.

Configured

- PostgreSQL 16
- Database
- User
- Password
- Port Mapping

Environment Variables

```text
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
```

---

## 4. Database Initialization

Created database schema automatically during CI execution.

The workflow creates

```sql
employees
```

table before executing tests.

---

## 5. Code Quality

Integrated automated quality checks.

### Black

Checks code formatting

```bash
black --check .
```

---

### isort

Checks import ordering

```bash
isort --check-only .
```

---

### Flake8

Checks

- Style
- Syntax
- Best Practices

```bash
flake8 .
```

---

## 6. Automated Testing

Executed

```bash
pytest
```

Included

- Unit Tests
- Integration Tests

Integration tests connect to PostgreSQL created inside GitHub Actions.

---

## 7. Test Coverage

Generated

- coverage.xml
- HTML Coverage Report

Command

```bash
pytest --cov=src \
       --cov-report=xml \
       --cov-report=html
```

---

## 8. Upload Coverage

Coverage report uploaded as GitHub Artifact.

Artifacts can be downloaded after every successful workflow.

---

# CI Pipeline Flow

```text
Push Code
      │
      ▼
Checkout Repository
      │
      ▼
Setup Python
      │
      ▼
Install Dependencies
      │
      ▼
Start PostgreSQL
      │
      ▼
Wait Until Database Ready
      │
      ▼
Create Employees Table
      │
      ▼
Black
      │
      ▼
isort
      │
      ▼
Flake8
      │
      ▼
Run Unit Tests
      │
      ▼
Run Integration Tests
      │
      ▼
Generate Coverage
      │
      ▼
Upload Coverage Report
      │
      ▼
Pipeline Success
```

---

# Problems Faced

## Problem 1

GitHub Actions failed because

```
requirements-dev.txt
```

was missing.

### Solution

Merged all dependencies into

```
requirements.txt
```

---

## Problem 2

Black formatting failed.

### Solution

Executed

```bash
black .
```

Committed formatted code.

---

## Problem 3

Integration Tests failed.

Error

```
Connection Refused
```

Reason

GitHub runner did not have PostgreSQL.

### Solution

Started PostgreSQL service inside GitHub Actions.

---

## Problem 4

Database table missing.

### Solution

Added automatic table creation step inside workflow.

---

## Problem 5

Environment variables mismatch.

Application expected

```text
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
```

Workflow updated accordingly.

---

# Final Workflow Features

✔ Automatic Build

✔ Automatic PostgreSQL

✔ Automatic Table Creation

✔ Code Formatting Check

✔ Import Sorting

✔ Linting

✔ Unit Testing

✔ Integration Testing

✔ Coverage Generation

✔ Artifact Upload

---

# Commands Learned

Format

```bash
black .
```

Check Formatting

```bash
black --check .
```

Sort Imports

```bash
isort .
```

Check Imports

```bash
isort --check-only .
```

Lint

```bash
flake8 .
```

Run Tests

```bash
pytest
```

Coverage

```bash
pytest --cov=src
```

Coverage HTML

```bash
pytest --cov=src --cov-report=html
```

---

# Key Learning

Continuous Integration automatically validates code before merging.

Every push now performs

- Formatting validation
- Linting
- Testing
- Database initialization
- Coverage generation

This ensures production-quality code and reduces deployment failures.

---

# Repository Status

Current project includes

- Python ETL Pipeline
- Modular Architecture
- Logging
- Data Validation
- PostgreSQL
- Incremental Loading
- UPSERT
- Transaction Rollback
- Unit Testing
- Integration Testing
- Code Coverage
- Black
- isort
- Flake8
- GitHub Actions CI/CD

---

# Outcome

The GitHub Actions pipeline executes successfully with

- PostgreSQL service
- Automated schema creation
- Complete test suite
- Code quality validation
- Coverage report generation

The project is now production-ready from a Continuous Integration perspective.

---

# Next Session (Day 10 – Part 2)

Remaining work

- Professional README.md
- Mermaid Architecture Diagram
- CHANGELOG.md
- CONTRIBUTING.md
- LICENSE
- .env.example
- GitHub Release v1.0.0
- Final Portfolio Review

---

# Mentor Remarks

This marks the completion of the engineering phase of the Python ETL project.

The repository now demonstrates:

- Software Engineering Best Practices
- Production ETL Design
- Automated Testing
- Continuous Integration
- Database Automation
- Professional Project Structure

The next session will focus on documentation, presentation, and preparing the repository as a portfolio-quality project for interviews.
