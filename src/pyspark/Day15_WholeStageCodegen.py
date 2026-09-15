from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Day15_Part8_WholeStageCodegen")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("datasets/employees.csv")
)

# result = (
#     df
#     .filter(df.salary > 50000)
#     .select("name", "department", "salary")
# )

result = (
    df
    .filter(df.salary > 50000)
    .select("name", "department", "salary")
    .groupBy("department")
    .count()
)

result.explain(True)

result.count()

input("\nPress Enter to stop...")
