from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Day13_SparkUI_Execution").getOrCreate()


df = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv("datasets/employees.csv")
)


# ============================================================
# 1. DataFrame Basic Information
# ============================================================

# df.printSchema()

# print("Columns:", df.columns)

# print("Data Types:", df.dtypes)

# print("Schema:", df.schema)


# ============================================================
# 2. Lazy Evaluation - Transformation Only
# ============================================================

# filtered_df = df.filter(df.salary > 50000)

# print("Transformation created.")
# print("No action has been executed yet.")

# input("\nPress Enter to stop...")


# ============================================================
# 3. Action - show()
# ============================================================

# filtered_df = df.filter(df.salary > 50000)

# filtered_df.show()

# input("\nPress Enter to stop...")


# ============================================================
# 4. count() Action
# ============================================================

# filtered_df = df.filter(df.salary > 50000)

# print("Count:", filtered_df.count())

# input("\nPress Enter to stop...")


# ============================================================
# 5. Partition Count
# ============================================================

# print("Original Partitions:", df.rdd.getNumPartitions())

# input("\nPress Enter to stop...")


# ============================================================
# 6. repartition(4)
# ============================================================

# repartitioned_df = df.repartition(4)

# print("Partitions after repartition:",
#       repartitioned_df.rdd.getNumPartitions())

# input("\nPress Enter to stop...")


# ============================================================
# 7. repartition(4) + Action
#    Observe Shuffle in Spark UI
# ============================================================

# repartitioned_df = df.repartition(4)

# print("Partitions:",
#       repartitioned_df.rdd.getNumPartitions())

# print("Count:", repartitioned_df.count())

# input("\nPress Enter to stop...")


# ============================================================
# 8. Filter After Repartition
#    Observe Stage / Tasks / Shuffle
# ============================================================

# repartitioned_df = df.repartition(4)

# filtered_df = repartitioned_df.filter(
#     repartitioned_df.salary > 90000
# )

# filtered_df.show()

# input("\nPress Enter to stop...")


# ============================================================
# 9. Task Concurrency Experiment
#    Use Spark UI to observe tasks and executor cores
# ============================================================

# repartitioned_df = df.repartition(20)

# print("Partitions:",
#       repartitioned_df.rdd.getNumPartitions())

# print("Count:", repartitioned_df.count())

# input("\nPress Enter to stop...")


# ============================================================
# 10. Shuffle Write / Shuffle Read
# ============================================================

# repartitioned_df = df.repartition(4)

# repartitioned_df.count()

# input("\nPress Enter to stop...")


# ============================================================
# 11. groupBy() - Shuffle Experiment
# ============================================================

grouped_df = df.groupBy("department").count()

grouped_df.show()

input("\nPress Enter to stop...")


# ============================================================
# 12. Cache - Mark Only
# ============================================================

# cached_df = df.repartition(4)

# cached_df.cache()

# print("Cache marked.")

# print(
#     "Partitions:",
#     cached_df.rdd.getNumPartitions()
# )

# input("\nPress Enter to stop...")


# ============================================================
# 13. Cache + Action - Materialize Cache
# ============================================================

# cached_df = df.repartition(4)

# cached_df.cache()

# print("Cache marked.")

# print("Count:", cached_df.count())

# input("\nPress Enter to stop...")


# ============================================================
# 14. Cache + Repeated Action
# ============================================================

# cached_df = df.repartition(4)

# cached_df.cache()

# print("First Count:", cached_df.count())

# print("Second Count:", cached_df.count())

# input("\nPress Enter to stop...")


# ============================================================
# 15. Cache + Filter
# ============================================================

# cached_df = df.repartition(4)

# cached_df.cache()

# cached_df.count()

# filtered_df = cached_df.filter(
#     cached_df.salary > 90000
# )

# filtered_df.show()

# input("\nPress Enter to stop...")


# ============================================================
# 16. DataFrame describe()
# ============================================================

# df.describe().show()

# input("\nPress Enter to stop...")


# ============================================================
# 17. Explain - Introduction
#    This is only an introduction on Day 13.
#    Detailed Explain Plans are Day 14.
# ============================================================

# df.explain()

# input("\nPress Enter to stop...")


# ============================================================
# 18. Combined Execution Experiment
#    Transformation + repartition + filter + action
# ============================================================

# experiment_df = df.repartition(4)

# experiment_df = experiment_df.filter(
#     experiment_df.salary > 90000
# )

# experiment_df.show()

# input("\nPress Enter to stop...")


# ============================================================
# 19. Cleanup
# ============================================================

# spark.stop()
