# Day 12 - Mermaid Diagrams
## Phase 2 - Big Data Engineering with PySpark

This document contains all Mermaid diagrams used during Day 12.

---

# 1. Spark Application Architecture

```mermaid
graph TD

A[Python Application] --> B[SparkSession]
B --> C[SparkContext]
C --> D[Driver Process]
D --> E[Cluster Manager]
E --> F[Executor]
F --> G[Task]
```

---

# 2. Spark Application Lifecycle

```mermaid
graph TD

A[Python Starts]
A --> B[SparkSession.builder]
B --> C[getOrCreate]
C --> D[SparkSession Created]
D --> E[SparkContext Created]
E --> F[Driver Process Started]
F --> G[Application Ready]
G --> H[Waiting for Action]
```

---

# 3. Lazy Evaluation

```mermaid
graph TD

A["spark.read.csv"]
--> B["filter"]
--> C["select"]
--> D["withColumn"]
--> E["Logical Plan"]

style E fill:#FFD966
```

---

# 4. Action Triggers Execution

```mermaid
graph TD

A[Logical Plan]
--> B["Action : df.show"]
--> C[Job Created]
--> D[Stage Created]
--> E[Tasks Created]
--> F[Executors Execute]
--> G[Result Returned]

style B fill:#A4C2F4
style C fill:#F4CCCC
style G fill:#B6D7A8
```

---

# 5. Spark Execution Hierarchy

```mermaid
graph TD

A[Action]
--> B[Job]
--> C[Stage]
--> D[Task]
```

---

# 6. Complete Spark Execution Flow

```mermaid
graph TD

A[Python Code]
--> B[SparkSession]
--> C[SparkContext]
--> D[Driver Process]
--> E[Logical Plan]
--> F[Action]
--> G[Job]
--> H[Stage]
--> I[Tasks]
--> J[Executors]
--> K[Result]
```

---

# 7. Driver and Executors

```mermaid
graph TD

A[Driver]

A --> B[Executor 1]
A --> C[Executor 2]
A --> D[Executor 3]

B --> E[Task 1]
B --> F[Task 2]

C --> G[Task 3]
C --> H[Task 4]

D --> I[Task 5]
D --> J[Task 6]
```

---

# 8. Partitions → Tasks

```mermaid
graph TD

A[employees.csv]

A --> B[Partition 1]
A --> C[Partition 2]
A --> D[Partition 3]
A --> E[Partition 4]

B --> F[Task 1]
C --> G[Task 2]
D --> H[Task 3]
E --> I[Task 4]
```

---

# 9. Parallel Task Execution

```mermaid
graph TD

A[Executor - 8 Cores]

A --> B[Core 1]
A --> C[Core 2]
A --> D[Core 3]
A --> E[Core 4]
A --> F[Core 5]
A --> G[Core 6]
A --> H[Core 7]
A --> I[Core 8]

B --> J[Task 1]
C --> K[Task 2]
D --> L[Task 3]
E --> M[Task 4]
F --> N[Task 5]
G --> O[Task 6]
H --> P[Task 7]
I --> Q[Task 8]
```

---

# 10. Task Scheduling in Waves

```mermaid
graph TD

A[32 Tasks]

A --> B[Wave 1<br/>Task 1-8]
A --> C[Wave 2<br/>Task 9-16]
A --> D[Wave 3<br/>Task 17-24]
A --> E[Wave 4<br/>Task 25-32]

B --> F[Executor]
C --> F
D --> F
E --> F
```

---

# 11. Local Mode vs Distributed Mode

```mermaid
graph LR

A[Local Mode]

A --> B[Driver]
B --> C[Executor]
C --> D[Laptop CPU Cores]

E[Cluster Mode]

E --> F[Driver]
F --> G[Cluster Manager]

G --> H[Executor 1]
G --> I[Executor 2]
G --> J[Executor 3]
```

---

# 12. Pandas vs Spark

```mermaid
graph LR

A[Pandas]

A --> B[Read CSV]
B --> C[Load Entire Data into RAM]
C --> D[Process Data]

E[Spark]

E --> F[Read CSV]
F --> G[Logical Plan]
G --> H[Action]
H --> I[Read Data]
I --> J[Distributed Processing]
```

---

# 13. Complete Day 12 Summary Diagram ⭐

```mermaid
graph TD

A[Python Application]
--> B[SparkSession]
--> C[SparkContext]
--> D[Driver Process]
--> E[Build Logical Plan]

E --> F["Action : df.show"]

F --> G[Job]

G --> H[Stage]

H --> I[Partition 1]
H --> J[Partition 2]
H --> K[Partition 3]
H --> L[Partition 4]

I --> M[Task 1]
J --> N[Task 2]
K --> O[Task 3]
L --> P[Task 4]

M --> Q[Executor]
N --> Q
O --> Q
P --> Q

Q --> R[Results Returned]
```

---

# Day 12 Key Takeaways

- SparkSession is the entry point.
- SparkContext communicates with the cluster.
- Driver coordinates execution.
- DataFrames store a Logical Plan.
- Lazy Evaluation delays execution.
- Actions trigger execution.
- Actions create Jobs.
- Jobs are divided into Stages.
- Stages are divided into Tasks.
- One Partition creates One Task.
- Executors execute Tasks.
- Parallelism depends on Partitions and available CPU Cores.
- Spark executes Tasks in waves when Tasks > Available Cores.
