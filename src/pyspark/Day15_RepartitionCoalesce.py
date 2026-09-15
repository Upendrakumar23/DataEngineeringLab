from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Day15_Part7_RepartitionCoalesce")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("datasets/employees.csv")
)

# Check original number of partitions
print("Original partitions:", df.rdd.getNumPartitions())


# --------------------------------------------------
# 1. repartition()
# --------------------------------------------------

repartitioned_df = df.repartition(4)

print(
    "After repartition:",
    repartitioned_df.rdd.getNumPartitions()
)

repartitioned_df.explain()


# --------------------------------------------------
# 2. coalesce()
# --------------------------------------------------

coalesced_df = repartitioned_df.coalesce(2)

print(
    "After coalesce:",
    coalesced_df.rdd.getNumPartitions()
)

coalesced_df.explain()


# --------------------------------------------------
# 3. repartition by column
# --------------------------------------------------

department_df = df.repartition(4, "department")

print(
    "After repartition by department:",
    department_df.rdd.getNumPartitions()
)

department_df.explain()


# Trigger execution
department_df.count()

input("\nPress Enter to stop...")
