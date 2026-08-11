from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read Employee CSV").getOrCreate()

df = spark.read.option("header", True).csv("datasets/employees.csv")

df = df.repartition(4)

filtered_df = df.filter(df.salary > 90000)

result = filtered_df.count()

print("Matching records:", result)

input("\nPress Enter to stop Spark...")
