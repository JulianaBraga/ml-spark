from pyspark.sql import SparkSession
from pyspark.sql import functions as f

spark = SparkSession \
        .builder \
        .appName("Regressão com Spark") \
        .getOrCreate()


