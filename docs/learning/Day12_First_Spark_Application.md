# Day 12 - First Spark Application

## Phase 2 - Big Data Engineering with PySpark

---

# Learning Objectives

Today we learned:

- SparkSession
- SparkContext
- Driver Process
- First Spark Application
- Reading CSV using Spark
- DataFrame Basics
- Lazy Evaluation
- Actions vs Transformations
- Jobs
- Stages
- Tasks
- Partitions
- Parallel Processing
- Spark Execution Flow

---

# Spark Architecture Overview

```
                Your Python Code
                       │
                       ▼
                SparkSession
                       │
                SparkContext
                       │
                       ▼
                 Driver Process
                       │
                       ▼
               Cluster Manager
                       │
                       ▼
                  Executors
                       │
                       ▼
                     Tasks
```

---

# SparkSession

SparkSession is the unified entry point introduced in Spark 2.x.

It provides access to

- DataFrame API
- SQL API
- Catalog
- SparkContext
- Configuration

Example

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("First Spark Application")
    .getOrCreate()
)
```

---

# SparkContext

SparkContext is responsible for

- communicating with the cluster
- scheduling jobs
- creating RDDs
- resource coordination

It is available through

```python
spark.sparkContext
```

---

# Driver Process

The Driver Process is responsible for

- executing Python code
- creating SparkSession
- creating SparkContext
- creating execution plans
- communicating with executors
- collecting results

The Driver does NOT process data.

Executors perform data processing.

---

# First Spark Application

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Read Employee CSV")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .csv("datasets/employees.csv")
)

print("DataFrame Created")

df.show()

spark.stop()
```

---

# Application Lifecycle

```
Python Starts

↓

SparkSession.builder

↓

getOrCreate()

↓

SparkContext Created

↓

Driver Started

↓

Spark Application Ready
```

At this point

No Job exists.

---

# DataFrame

A Spark DataFrame does NOT immediately contain data.

Instead it contains a logical execution plan.

Conceptually

```
DataFrame

↓

Logical Plan

↓

Read employees.csv
```

---

# Lazy Evaluation

The following operations DO NOT execute immediately.

```python
df = spark.read.csv(...)

df = df.filter(...)

df = df.select(...)

df = df.withColumn(...)
```

Spark only records the operations.

---

# Action

An Action triggers execution.

Examples

```python
df.show()

df.count()

df.collect()

df.write.csv(...)
```

Once an Action is encountered

Spark creates

- Job
- Stage
- Tasks

---

# Spark Execution Hierarchy

```
Action

↓

Job

↓

Stage

↓

Task
```

Remember

No Action

↓

No Job

↓

No Stage

↓

No Task

---

# Execution Flow

```
DataFrame Created

↓

Logical Plan

↓

Action

↓

Job

↓

Stage

↓

Tasks

↓

Executors

↓

Driver

↓

Output
```

---

# Jobs

A Job is created ONLY after an Action.

Example

```python
df.show()
```

creates

Job 0

---

# Stage

A Stage is a group of Tasks.

Without Shuffle

Usually

```
Job

↓

Stage 0
```

---

# Task

Task is the smallest execution unit in Spark.

One Partition

↓

One Task

---

# Important Rule

One Partition

↓

One Task

NOT

One File

↓

One Task

---

# Parallel Processing

Suppose

```
Executor

8 CPU Cores

32 Tasks
```

Execution

```
Wave 1

Task 1-8

↓

Wave 2

Task 9-16

↓

Wave 3

Task 17-24

↓

Wave 4

Task 25-32
```

Tasks execute according to available CPU cores.

---

# Local Mode vs Distributed Mode

Local Mode

```
Laptop

↓

Driver

↓

Executor

↓

CPU Cores
```

Parallel

YES

Distributed

NO

---

Spark Standalone

```
Spark Master

↓

Workers

↓

Executors
```

Parallel

YES

Distributed

YES

---

Kubernetes

```
Driver

↓

Kubernetes

↓

Executor Pods
```

Cloud Native

Distributed

YES

---

# Pandas vs Spark (Concept)

Pandas

```
Read CSV

↓

Immediately loads data into RAM
```

Spark

```
Read CSV

↓

Creates Logical Plan

↓

Reads data only after Action
```

---

# Key Learnings

- SparkSession is the entry point.
- SparkContext communicates with the cluster.
- Driver coordinates execution.
- Executors process data.
- DataFrame stores a logical plan.
- Spark uses Lazy Evaluation.
- Actions trigger execution.
- Jobs contain Stages.
- Stages contain Tasks.
- One Partition creates One Task.
- Spark parallelism depends on Partitions and CPU cores.

---

# Interview Questions

### Q1

Does SparkSession create a Job?

Answer

No.

It only initializes the Spark application.

---

### Q2

Does read.csv() read the file immediately?

Answer

No.

Spark creates a logical plan.

---

### Q3

What triggers execution?

Answer

Actions.

---

### Q4

Can Spark create more Tasks than CPU cores?

Answer

Yes.

Tasks execute in multiple waves.

---

### Q5

What determines the number of Tasks?

Answer

Number of Partitions.

---

### Q6

If a file has one partition and the executor has 16 cores, will Spark use all cores?

Answer

No.

Only one Task exists.

Therefore only one core is utilized.

---

# Today's Achievement

Today we moved from

"I know PySpark syntax"

to

"I understand how Spark executes a program."

This is the foundation required before learning

- Catalyst Optimizer
- Shuffle
- Partitioning
- Performance Tuning
- Spark UI
