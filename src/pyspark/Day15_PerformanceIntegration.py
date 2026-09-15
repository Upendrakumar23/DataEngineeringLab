from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
    "Day15_Part11_PerformanceIntegration"
).getOrCreate()

# --------------------------------------------------
# Spark configuration
# --------------------------------------------------

print("AQE enabled:", spark.conf.get("spark.sql.adaptive.enabled"))

print("Shuffle partitions:", spark.conf.get("spark.sql.shuffle.partitions"))


# --------------------------------------------------
# Read data
# --------------------------------------------------

df = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv("datasets/employees.csv")
)

print("Input partitions:", df.rdd.getNumPartitions())


# --------------------------------------------------
# Filter
# --------------------------------------------------

filtered_df = df.filter(df.salary > 50000)


# --------------------------------------------------
# Aggregation
# --------------------------------------------------

result = filtered_df.groupBy("department").count()


# --------------------------------------------------
# Explain execution plan
# --------------------------------------------------

print("\n========== EXECUTION PLAN ==========\n")

result.explain(True)


# --------------------------------------------------
# Trigger execution
# --------------------------------------------------

print("\n========== RESULT ==========\n")

result.show()


# --------------------------------------------------
# Keep Spark UI available
# --------------------------------------------------

input(
    "\nOpen http://localhost:4040 to inspect Spark UI. " "Press Enter to stop Spark..."
)

spark.stop()
