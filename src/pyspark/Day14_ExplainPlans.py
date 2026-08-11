from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Day14_ExplainPlans").getOrCreate()

df = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv("datasets/employees.csv")
)


# df.printSchema()
# df.explain()
# df.explain(True)

# filtered_df = df.filter(df.salary > 50000)
# filtered_df.explain(True)

# selected_df = df.select("name", "salary")
# selected_df.explain(True)

# result_df = (
#     df
#     .filter(df.salary > 50000)
#     .select("name", "salary")
# )
# result_df.explain(True)

# df.repartition(4).explain(True)

# repartitioned_df = df.repartition(4)
# repartitioned_df.count()

grouped_df = df.groupBy("department").count()
grouped_df.explain(True)


input("\nPress Enter to stop...")
