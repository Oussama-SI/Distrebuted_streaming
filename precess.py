from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LocalClusterProcessing") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

print(spark)

# # Load data
# df = spark.read.parquet("/opt/spark-data/yellow_tripdata_2024-01.parquet")

# # Sample transformation
# result = df.groupBy("PULocationID").count().orderBy("count", ascending=False)

# result.show(10)

# # Write output
# result.write.mode("overwrite").parquet("/opt/spark-data/output/")
