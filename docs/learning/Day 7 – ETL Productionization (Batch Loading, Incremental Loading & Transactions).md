# Day 7 – ETL Productionization (Batch Loading, Incremental Loading & Transactions)

**Project:** DataEngineeringLab

---

# Objectives

Today's goal was to make the ETL pipeline production-ready by improving the data loading process.

Modules covered:

* Batch Loading
* Incremental Loading (UPSERT)
* Transaction Management
* ETL Execution Summary
* Production Exception Handling

---

# Module 1 – Batch Loading

## Why?

Loading one record at a time is inefficient because every `cursor.execute()` call sends a separate request to PostgreSQL.

For large datasets this results in:

* More network round trips
* Higher execution time
* Poor scalability

---

## Approaches Compared

### 1. Row-by-Row Loading

```python
cursor.execute(...)
```

Characteristics:

* Simple
* Easy to understand
* Slow for large datasets

---

### 2. Single `executemany()`

```python
cursor.executemany(query, data)
```

Benefits:

* One database API call
* Better performance
* Less Python overhead

---

### 3. Batch Loading

```python
for batch in batches:
    cursor.executemany(query, batch)
```

Benefits:

* Lower memory usage
* Better scalability
* Easier monitoring
* Production-friendly

---

## Performance Benchmark

| Method              | Rows |      Time |
| ------------------- | ---: | --------: |
| execute()           | 5000 | ~1.57 sec |
| executemany()       | 5000 | ~0.51 sec |
| Batch executemany() | 5000 | ~0.30 sec |

---

# Module 2 – Incremental Loading (UPSERT)

## Why?

Reloading the entire table every day wastes:

* CPU
* Disk I/O
* Transaction logs
* Database resources

Instead, update existing records and insert only new ones.

---

## Primary Key vs Business Key

Primary Key

* Database generated
* Internal identifier

Business Key

* Comes from source system
* Used for synchronization

In this project:

```
employee_code
```

is the Business Key.

---

## PostgreSQL UPSERT

Used:

```sql
ON CONFLICT (employee_code)
DO UPDATE
```

This allows:

* Insert new employees
* Update existing employees
* Prevent duplicate records

---

## Testing Completed

### Initial Load

Inserted 5 employees.

✅ Passed

---

### Re-run Same File

No duplicate records created.

✅ Passed

---

### Incremental Load

Added:

* EMP006
* EMP007
* EMP008
* EMP009
* EMP010

Only new employees were inserted.

✅ Passed

---

### Update Existing Employee

Updated salary for:

* EMP003
* EMP004

Existing records were updated without changing the row count.

✅ Passed

---

## Key Learning

The ETL became **idempotent**.

Running the same file multiple times produces the correct database state without creating duplicates.

---

# Module 3 – Transaction Management

## Why?

A database transaction ensures that either:

* all changes are committed

or

* none of them are committed

---

## Transaction Flow

```
Start Transaction

↓

Load Data

↓

Commit

or

Rollback
```

---

## ACID Principle Learned

Focused on:

Atomicity

```
All

or

Nothing
```

Never partial data.

---

## Transaction Functions

### commit()

Makes database changes permanent.

---

### rollback()

Restores the database to its previous consistent state if an error occurs.

---

## Production Strategy

Current implementation:

* Single transaction
* Single commit
* Full rollback on failure

Suitable for small and medium ETL jobs.

---

# Module 4 – ETL Execution Summary

Implemented execution metrics including:

* Pipeline Name
* Source File
* Load Strategy
* Rows Extracted
* Rows Validated
* Rows Transformed
* Rows Processed
* Batch Size
* Number of Batches
* Start Time
* End Time
* Duration
* Status

---

## Responsibility Separation

### load_incremental.py

Responsible for:

* Database connection
* UPSERT
* Commit / Rollback
* Returning processed row count

---

### main.py

Responsible for:

* Orchestration
* Timing
* Collecting metrics
* Printing the final execution summary

---

# Module 5 – Production Exception Handling

Improved exception handling strategy.

Different error categories:

* File errors
* Validation errors
* Database errors
* Unexpected errors

---

## Fail Fast Principle

Pipeline flow:

```
Validate File

↓

Extract

↓

Validate Data

↓

Transform

↓

Load
```

If any stage fails, the pipeline stops immediately.

No invalid data reaches the database.

---

# Final ETL Architecture

```
CSV
    │
    ▼
File Validation
    │
    ▼
Extraction
    │
    ▼
Data Validation
    │
    ▼
Transformation
    │
    ▼
Batch UPSERT
    │
    ▼
PostgreSQL
    │
    ▼
Execution Summary
```

---

# Skills Gained

* Modular ETL Design
* Configuration Management
* Structured Logging
* Data Validation Framework
* Batch Loading
* PostgreSQL executemany()
* Incremental Loading
* PostgreSQL UPSERT
* Idempotent ETL
* Transaction Management
* Execution Summary
* Production Exception Handling

---

# Day 7 Outcome

The ETL pipeline is now significantly closer to a production-ready implementation.

Key production capabilities achieved:

* Modular architecture
* Batch processing
* Incremental loading
* Transaction safety
* Execution reporting
* Structured logging
* Better exception handling

The pipeline is now ready for the next phase of the Data Engineering learning roadmap.
