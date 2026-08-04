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
