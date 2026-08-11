from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Pure Cache Demo").getOrCreate()

df = spark.read.option("header", True).csv("datasets/employees.csv")

df = df.repartition(4)

df.cache()

print("Cache marked.")

result = df.count()

print("Count:", result)

input("\nPress Enter to stop...")
