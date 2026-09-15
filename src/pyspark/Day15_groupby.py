from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Day15_groupby").getOrCreate()

df = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv("datasets/employees.csv")
)


grouped_df = df.groupBy("department").count()
# grouped_df.explain(True)
# grouped_df.show()
grouped_df.count()


input("\nPress Enter to stop...")
