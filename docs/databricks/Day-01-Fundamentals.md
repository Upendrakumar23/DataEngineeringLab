# Databricks Certification – Day 1
## Fundamentals and Lakehouse Architecture

**Target Certification:** Databricks Certified Data Engineer Associate  
**Target Exam Date:** September 30, 2026  
**Learning Track:** Databricks Certification  
**Status:** Completed

---

# 1. Day 1 Objectives

Today we covered the fundamental Databricks concepts required before starting the detailed Delta Lake preparation.

### Topics Covered

- What is Databricks?
- Data Lake
- Lakehouse
- Delta Lake
- Databricks Workspace
- Compute
- Notebooks
- Databricks SQL
- Unity Catalog
- Managed vs External Tables
- Three-level namespace
- Data Lake vs Delta Lake vs Lakehouse
- Databricks overall architecture
- Certification-style questions

---

# 2. What is Databricks?

Databricks is a data and AI platform built around Apache Spark and the Lakehouse architecture.

For a Data Engineer, important Databricks components include:

- Workspace
- Compute
- Notebooks
- Databricks SQL
- Delta Lake
- Unity Catalog
- Lakeflow Jobs
- Data ingestion and transformation capabilities

A simplified view:

```text
                    DATABRICKS
                        |
       +----------------+----------------+
       |                |                |
   Workspace         Compute       Unity Catalog
       |                |                |
 notebooks/SQL      Executes        Governance
                    workloads
       |                |
       +----------------+
                |
            Lakehouse
                |
           Delta Lake
                |
        Cloud Storage
```

---

# 3. Data Lake

A Data Lake is a flexible storage environment used to store large amounts of data in different formats.

Examples:

- CSV
- JSON
- Parquet
- Application logs
- IoT data
- Images
- Raw source data
- Structured and semi-structured data

Typical cloud storage technologies include:

- Amazon S3
- Azure Data Lake Storage
- Google Cloud Storage

Example:

```text
                    DATA LAKE
                        |
        +---------------+---------------+
        |               |               |
       CSV             JSON           Parquet
        |               |               |
        +---------------+---------------+
                        |
                 Cloud Storage
```

## Advantages

- Flexible
- Can store many data formats
- Suitable for large-scale data
- Relatively inexpensive object storage
- Can store raw and processed data

## Traditional Data Lake Challenges

A basic collection of files does not inherently provide the same transactional and table-management capabilities expected from a modern analytical platform.

Historically, common challenges included:

- ACID transactions
- Concurrent writes
- Reliable UPDATE operations
- Reliable DELETE operations
- MERGE/upsert operations
- Schema enforcement
- Schema evolution
- Data versioning
- Consistency

This is where Delta Lake becomes important.

---

# 4. Delta Lake

Delta Lake is a storage/table layer that adds reliability and transactional capabilities to data stored in a data lake.

Delta Lake commonly uses:

- Parquet files for the actual data
- `_delta_log` for transaction information

Conceptually:

```text
                  DELTA TABLE
                       |
          +------------+------------+
          |                         |
          v                         v
   Parquet data files          _delta_log
                               transaction log
```

Example:

```text
employees/
|
+-- part-00000.parquet
+-- part-00001.parquet
+-- part-00002.parquet
|
+-- _delta_log/
      |
      +-- 000000.json
      +-- 000001.json
      +-- 000002.json
      +-- ...
```

---

# 5. Why Do We Need Delta Lake?

A Data Lake gives us flexible storage.

However, Data Engineers also need reliable table operations.

For example:

```sql
UPDATE employees
SET salary = salary * 1.10
WHERE department = 'IT';
```

Or:

```sql
DELETE FROM employees
WHERE employee_id = 100;
```

Or an upsert:

```sql
MERGE INTO target
USING source
ON target.id = source.id
WHEN MATCHED THEN
  UPDATE SET *
WHEN NOT MATCHED THEN
  INSERT *;
```

Delta Lake provides the table-management and transaction capabilities needed to perform these operations reliably.

---

# 6. Important Delta Lake Capabilities

Delta Lake supports important capabilities such as:

- ACID transactions
- Schema enforcement
- Schema evolution
- UPDATE
- DELETE
- MERGE
- Time Travel
- Reliable concurrent operations

These are major certification topics.

We will study them in detail on Day 2.

---

# 7. Lakehouse

Lakehouse is an overall **data architecture**.

The Lakehouse concept combines:

```text
Data Lake
    +
Data Warehouse capabilities
```

The goal is to provide the flexibility of a data lake while supporting reliable analytics and data management capabilities commonly associated with data warehouses.

Conceptually:

```text
                     LAKEHOUSE
                  (Architecture)
                        |
        +---------------+---------------+
        |                               |
        v                               v
 Data Lake Characteristics       Warehouse Capabilities
        |                               |
 Flexible storage                 SQL analytics
 Raw + structured                 Reliability
 Large-scale data                 Transactions
 Open data formats                Governance
        |                               |
        +---------------+---------------+
                        |
                   Delta Lake
```

---

# 8. Data Lake vs Delta Lake vs Lakehouse

These three concepts should NOT be treated as competing technologies.

They represent different layers/concepts.

| Concept | Meaning |
|---|---|
| Data Lake | Flexible data storage/architecture |
| Delta Lake | Reliable transactional table/storage layer |
| Lakehouse | Overall architecture combining lake flexibility with warehouse capabilities |

### Simple mental model

```text
                 LAKEHOUSE
                Architecture
                     |
                     v
                Delta Lake
                 Table Layer
                     |
          +----------+----------+
          |                     |
          v                     v
     Parquet files        Transaction log
          |                     |
          +----------+----------+
                     |
                     v
            Cloud Object Storage
             S3 / ADLS / GCS
```

---

# 9. Data Lake

### Think:

> "Where can I store lots of different types of data?"

Answer:

**Data Lake**

Example:

```text
CSV
JSON
Parquet
Logs
Images
IoT
Raw files
```

---

# 10. Delta Lake

### Think:

> "How can I make data-lake tables reliable and transactional?"

Answer:

**Delta Lake**

Important features:

```text
ACID
MERGE
UPDATE
DELETE
Time Travel
Schema enforcement
Schema evolution
```

---

# 11. Lakehouse

### Think:

> "What overall architecture combines data-lake flexibility with warehouse-style capabilities?"

Answer:

**Lakehouse**

---

# 12. Simple Analogy

Consider a warehouse business.

## Data Lake = Building

The building provides a large flexible place where you can store:

- Boxes
- Documents
- Raw materials
- Machines

It gives you storage, but not necessarily sophisticated inventory management.

## Delta Lake = Inventory Management System

The inventory system adds:

- Transaction records
- Version information
- Consistency
- Controlled updates
- History

## Lakehouse = Complete Architecture

The complete architecture combines:

```text
Building
+
Inventory management
+
Analytics
+
Reporting
+
Governance
```

Therefore:

```text
Data Lake
    ↓
Storage

Delta Lake
    ↓
Reliable transactional tables

Lakehouse
    ↓
Overall architecture
```

---

# 13. Databricks Workspace

The Databricks Workspace is the environment where users organize and work with Databricks resources.

Examples include:

- Notebooks
- SQL
- Git folders
- Other workspace objects
- Development resources

Think of Workspace as the environment in which the Data Engineer works.

```text
Workspace
|
+-- Notebooks
+-- SQL
+-- Git folders
+-- Other resources
```

### Important

Workspace is NOT the same thing as data storage.

---

# 14. Compute

Compute provides the resources required to execute workloads.

Example:

```python
df = spark.read.table("employees")

df.filter("salary > 50000").count()
```

Compute resources are used to execute the Spark workload.

Simplified:

```text
Notebook
   |
   v
Compute
   |
   v
Spark execution
   |
   v
Data
```

### Important distinction

```text
Compute
    ↓
Executes workload

Delta Lake
    ↓
Provides reliable table/storage capabilities
```

Compute does NOT exist to store Delta transaction logs.

---

# 15. Notebooks

Databricks notebooks provide an interactive environment for developing and executing data workloads.

Common languages include:

- Python
- SQL
- Scala
- R

Example Python:

```python
df = spark.read.table("employees")

df.filter("salary > 50000").show()
```

Example SQL:

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

Notebooks can be used for:

- Development
- Data exploration
- Transformation
- Testing
- Debugging
- Analysis

---

# 16. Databricks SQL

Databricks SQL provides a SQL-based environment for querying and analyzing data in the Lakehouse.

Example:

```sql
SELECT
    department,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

Databricks SQL is not simply a completely separate database.

It is a SQL interface for working with data in the Databricks Lakehouse environment.

---

# 17. Unity Catalog

Unity Catalog provides centralized governance for data and AI assets.

Important capabilities include:

- Access control
- Permissions
- Metadata
- Data lineage
- Governance

Simplified:

```text
                 Unity Catalog
                      |
        +-------------+-------------+
        |             |             |
    Catalogs       Schemas       Objects
        |             |             |
        +-------------+-------------+
                      |
              Access / Governance
```

---

# 18. Three-Level Namespace

A very important Databricks concept is:

```text
catalog.schema.object
```

Example:

```text
finance.reporting.transactions
```

Meaning:

```text
finance
   ↓
catalog

reporting
   ↓
schema

transactions
   ↓
table/view/object
```

Another example:

```text
marketing.gold.customers
```

Meaning:

```text
marketing  → catalog
gold       → schema
customers  → table/view/object
```

### Certification memory

Always remember:

```text
catalog.schema.object
```

---

# 19. Managed Tables

A managed table is a table where Databricks manages the table's data storage/lifecycle within the configured managed storage environment.

Conceptually:

```text
                 DATABRICKS
                     |
          +----------+----------+
          |                     |
          v                     v
     Table metadata        Table data
                               |
                        Managed storage
```

The exact physical storage location depends on the Databricks/cloud configuration.

---

# 20. External Tables

An external table references data stored at an externally specified storage location.

Conceptually:

```text
                 DATABRICKS
                     |
                     v
                Table metadata
                     |
                     v
             Existing cloud storage
```

The underlying data remains at the specified external storage location.

---

# 21. Managed vs External Table

| | Managed Table | External Table |
|---|---|---|
| Data storage | Databricks-managed storage configuration | Externally specified storage location |
| Data lifecycle | Managed by Databricks | Data location/lifecycle remains externally controlled |
| Existing external location | Usually not the main use case | Common use case |
| Key exam clue | Databricks manages storage/lifecycle | Keep data in existing external location |

### Certification clue

If the question says:

- Existing cloud-storage location
- Keep data where it is
- Do not move underlying data
- Existing external data
- Data is managed outside Databricks

Think:

**External Table**

---

# 22. Overall Databricks Mental Model

```text
                    DATABRICKS
                        |
       +----------------+----------------+
       |                |                |
       v                v                v
   Workspace          Compute       Unity Catalog
       |                |                |
       |                |                +-- Governance
       |                |
       |                +-- Execute workloads
       |
       +-- Notebooks
       +-- SQL
       +-- Git folders
                        |
                        v
                    Lakehouse
                        |
                        v
                   Delta Lake
                        |
              +---------+---------+
              |                   |
              v                   v
        Parquet files       _delta_log
              |                   |
              +---------+---------+
                        |
                        v
                Cloud Storage
             S3 / ADLS / GCS
```

---

# 23. Key Relationships

### Workspace

```text
Workspace
    ↓
Where we organize/work with Databricks resources
```

### Compute

```text
Compute
    ↓
Provides resources to execute workloads
```

### Delta Lake

```text
Delta Lake
    ↓
Reliable transactional table/storage layer
```

### Unity Catalog

```text
Unity Catalog
    ↓
Centralized governance
```

### Lakehouse

```text
Lakehouse
    ↓
Overall architecture
```

---

# 24. Certification Question – Q1

### Question

A company wants a platform that provides the flexibility of a data lake while also supporting reliable transactions and data warehouse-style analytics.

What Databricks concept addresses this requirement?

### Options

A. Workspace  
B. Lakehouse  
C. Compute  
D. Notebook

### Answer

**B. Lakehouse**

### Explanation

Lakehouse architecture combines data-lake flexibility with capabilities traditionally associated with data warehouses.

---

# 25. Certification Question – Q2

### Question

A data engineer writes:

```python
df = spark.read.table("sales")
df.filter("amount > 1000")
```

No action such as `show()` or `count()` is called.

Which statement is correct?

### Options

A. The cluster immediately executes the filter.

B. Spark creates the DataFrame transformation plan, but execution waits for an action.

C. The data is permanently filtered in the Delta table.

D. Unity Catalog executes the filter.

### Answer

**B. Spark creates the DataFrame transformation plan, but execution waits for an action.**

### Explanation

Spark transformations are lazily evaluated.

Examples of actions include:

```python
df.show()
df.count()
df.collect()
```

---

# 26. Certification Question – Q3

### Question

Which component is primarily responsible for centralized data governance, permissions and lineage?

### Options

A. Delta Lake  
B. Spark  
C. Unity Catalog  
D. Workspace

### Answer

**C. Unity Catalog**

---

# 27. Certification Question – Q4

### Question

What does this represent?

```text
finance.reporting.transactions
```

### Answer

```text
finance       → catalog
reporting     → schema
transactions  → table/view/object
```

General pattern:

```text
catalog.schema.object
```

---

# 28. Certification Question – Q5

### Question

Which statement best describes Delta Lake?

### Options

A. A replacement for Apache Spark

B. A cloud object storage service

C. A storage/table layer that adds reliability and transactional capabilities to data stored in the data lake

D. A Databricks notebook environment

### Answer

**C. A storage/table layer that adds reliability and transactional capabilities to data stored in the data lake**

---

# 29. Certification Question – Q6

### Question

Your organization already has data stored in a specific cloud-storage location.

They want to register and query the data from Databricks without moving the underlying data into Databricks-managed storage.

Would you generally consider a managed table or external table?

### Answer

**External table**

### Reason

The underlying data remains at an externally specified storage location.

### Certification clue

```text
Existing external data location
          ↓
Keep data where it is
          ↓
External Table
```

---

# 30. Certification Question – Q7

### Question

What is the primary purpose of Databricks compute?

### Options

A. Store Delta transaction logs

B. Provide resources to execute workloads

C. Manage user permissions

D. Store notebooks permanently

### Answer

**B. Provide resources to execute workloads**

### Important distinction

```text
Compute
    ↓
Executes workloads

Delta Lake
    ↓
Data + transaction capabilities

Unity Catalog
    ↓
Governance
```

---

# 31. Certification Question – Q8

### Question

What is the difference between Workspace and Unity Catalog?

### Answer

### Workspace

The Workspace is used to organize and work with resources such as:

- Notebooks
- SQL
- Git folders
- Other workspace objects

### Unity Catalog

Unity Catalog is used for centralized:

- Governance
- Permissions
- Access control
- Metadata
- Data lineage

---

# 32. Day 1 Self-Assessment

## Initial Quiz

| Question | Result |
|---|---|
| Q1 – Lakehouse | Correct |
| Q2 – Lazy evaluation | Correct |
| Q3 – Unity Catalog | Correct |
| Q4 – Namespace | Partially correct |
| Q5 – Delta Lake | Correct |
| Q6 – Managed vs External | Incorrect initially |
| Q7 – Compute | Incorrect initially |
| Q8 – Workspace vs Unity Catalog | Correct |

## Corrections Learned

### Namespace

```text
catalog.schema.object
```

### External Table

Existing data that should remain at an external storage location:

```text
External Table
```

### Compute

Compute:

```text
Executes workloads
```

It does not store Delta transaction logs.

### Delta Lake

Delta Lake:

```text
Provides reliable transactional table capabilities
```

It does not perform the computation itself.

---

# 33. Important Exam Memory Points

## Point 1 – Three-level namespace

```text
catalog.schema.object
```

---

## Point 2 – Data Lake

```text
Data Lake
    ↓
Flexible data storage
```

---

## Point 3 – Delta Lake

```text
Delta Lake
    ↓
Reliable transactional table layer
```

Important features:

```text
ACID
MERGE
UPDATE
DELETE
Time Travel
Schema enforcement
Schema evolution
```

---

## Point 4 – Lakehouse

```text
Lakehouse
    ↓
Overall architecture
    ↓
Data Lake flexibility
+
Warehouse capabilities
```

---

## Point 5 – Workspace

```text
Workspace
    ↓
Organize/work with resources
```

---

## Point 6 – Compute

```text
Compute
    ↓
Execute workloads
```

---

## Point 7 – Unity Catalog

```text
Unity Catalog
    ↓
Governance
Permissions
Lineage
Metadata
```

---

## Point 8 – External Table

```text
Existing external storage
        ↓
Keep data in that location
        ↓
External Table
```

---

# 34. One-Page Revision

```text
                    DATABRICKS
                        |
       +----------------+----------------+
       |                |                |
   Workspace          Compute       Unity Catalog
       |                |                |
   Organize          Execute         Governance
   resources         workloads
       |
       +-- Notebooks
       +-- SQL
       +-- Git
                        |
                        v
                    Lakehouse
                  (Architecture)
                        |
                        v
                   Delta Lake
                  (Table Layer)
                        |
              +---------+---------+
              |                   |
          Parquet             _delta_log
          data files        transaction log
              |                   |
              +---------+---------+
                        |
                        v
                 Cloud Storage
                S3 / ADLS / GCS
```

---

# 35. Day 1 Final Takeaways

The most important distinction is:

```text
Data Lake
    =
Flexible storage/architecture

Delta Lake
    =
Reliable transactional table layer

Lakehouse
    =
Overall architecture combining lake flexibility
with warehouse capabilities
```

And:

```text
Workspace
    =
Organize and work with resources

Compute
    =
Execute workloads

Unity Catalog
    =
Governance

Delta Lake
    =
Reliable tables and transactions
```

---

# 36. Day 1 Status

- [x] Databricks overview
- [x] Data Lake
- [x] Lakehouse
- [x] Delta Lake
- [x] Workspace
- [x] Compute
- [x] Notebooks
- [x] Databricks SQL
- [x] Unity Catalog
- [x] Three-level namespace
- [x] Managed tables
- [x] External tables
- [x] Data Lake vs Delta Lake vs Lakehouse
- [x] Databricks architecture
- [x] Certification questions
- [x] Self-assessment

**Day 1: COMPLETED**

---

# Next: Day 2

## Delta Lake Deep Dive

Topics planned:

1. Parquet vs Delta
2. Delta table structure
3. `_delta_log`
4. Transactions
5. ACID
6. Delta table creation
7. INSERT
8. UPDATE
9. DELETE
10. MERGE
11. Time Travel
12. Schema enforcement
13. Schema evolution
14. OPTIMIZE
15. VACUUM
16. Managed vs External Delta tables
17. Certification scenarios
18. Practice questions

**Target:** Build a strong Delta Lake foundation for the Databricks Data Engineer Associate certification.
