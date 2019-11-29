from nsbu_data_cleanser.transformations.nsbu_transformations import NSBUTransformations
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf

spark_session = SparkSession.builder\
                    .appName("NSBU_DATA_JOB") \
                    .master("local[*]")\
                    .getOrCreate()

def print_each_line(eachLine):
    print eachLine
    return

def clean_spaces_column(data):
    return data.replace("4", "z")



csv_df = spark_session  .read\
                        .option("header", "true")\
                        .csv('/Users/dharshekthvel/ac/ddata/realdatav3.csv')


udf_myFunction = udf(clean_spaces_column, StringType())


cleaned_df = csv_df.withColumn("timestamp_cleaned", udf_myFunction("timestamp"))

cleaned_df.show()

