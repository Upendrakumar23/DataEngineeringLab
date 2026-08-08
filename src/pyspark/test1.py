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

df.filter(df.salary > 50000)
df.printSchema()
input("\nPress Enter to stop Spark...")
