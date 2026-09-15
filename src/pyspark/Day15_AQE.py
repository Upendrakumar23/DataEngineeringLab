from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Day15_Part9_AQE")
    .getOrCreate()
)

print(
    "AQE enabled:",
    spark.conf.get("spark.sql.adaptive.enabled")
)

print(
    "Shuffle partitions:",
    spark.conf.get("spark.sql.shuffle.partitions")
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("datasets/employees.csv")
)

result = (
    df
    .filter(df.salary > 50000)
    .groupBy("department")
    .count()
)

print("Before action:")
result.explain(True)

print("Triggering execution...")
result.show()

print("After action:")
result.explain(True)

spark.stop()
