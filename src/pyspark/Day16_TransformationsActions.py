from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Day16_TransformationsActions")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("datasets/employees.csv")
)

print("DataFrame created")

filtered_df = df.filter(df.salary > 80000)

print("Transformation created")

# filtered_df.show()

spark.stop()
