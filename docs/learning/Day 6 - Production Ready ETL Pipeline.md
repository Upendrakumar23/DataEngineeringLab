# Day 6 - Production Ready ETL Pipeline

## Objective

Convert the simple ETL pipeline into a modular, production-style application by introducing logging, configuration management, validation modules, and testing.

---

# Project Structure

```
DataEngineeringLab/
│
├── datasets/
│   ├── employees.csv
│   └── test/
│       ├── employees_blank.csv
│       ├── employees_duplicate.csv
│       ├── employees_invalid_salary.csv
│       ├── employees_missing_column.csv
│       └── employees_null.csv
│
├── logs/
│
├── src/
│   ├── config.py
│   ├── database.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── logger.py
│   ├── main.py
│   │
│   └── validations/
│       ├── validator.py
│       ├── file_validator.py
│       ├── schema_validator.py
│       ├── null_validator.py
│       ├── blank_validator.py
│       ├── duplicate_validator.py
│       └── salary_validator.py
│
└── tests/
```

---

# Topics Covered

## 1. Configuration Management

- Centralized application configuration
- Environment variable handling
- Dataset directory configuration
- Required schema configuration

---

## 2. Logging

Implemented application logging.

Features:

- Console logging
- File logging
- Exception logging
- Standard log formatting

---

## 3. Modular ETL

Separated the pipeline into independent modules.

- Extract
- Transform
- Load

Each module has a single responsibility.

---

## 4. Data Validation Framework

Implemented production-style validation modules.

### File Validator

Checks:

- Source file exists

---

### Schema Validator

Checks:

- Required columns are present

---

### Null Validator

Checks:

- Required columns do not contain NULL values

---

### Blank Validator

Checks:

- Text columns do not contain blank or whitespace values

---

### Duplicate Validator

Checks:

- Employee Code is unique

---

### Salary Validator

Checks:

- Salary is numeric
- Salary is greater than zero

---

### Master Validator

Runs all validations in sequence.

---

# Final ETL Flow

```
Validate File
      │
      ▼
Extract CSV
      │
      ▼
Validate Data
      │
      ├── Schema
      ├── Null
      ├── Blank
      ├── Duplicate
      └── Salary
      │
      ▼
Transform
      │
      ▼
Load into PostgreSQL
```

---

# Testing

Created tests for:

- Config
- Database
- Logger
- Extract
- Transform
- File Validator
- Schema Validator
- Null Validator
- Blank Validator
- Duplicate Validator
- Salary Validator
- Master Validator

Both positive and negative scenarios were tested.

---

# Learning Outcomes

- Modular Python architecture
- Logging
- Configuration management
- Data validation
- Error handling
- Clean project structure
- Production-style ETL workflow
- Unit-style testing

---

# Result

Successfully executed the complete ETL pipeline.

CSV
↓

Validated

↓

Transformed

↓

Loaded into PostgreSQL

Pipeline executed successfully with logging and validations.