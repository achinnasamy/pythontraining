
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.functions import lag
from pyspark.sql.functions import lead
from pyspark.sql.functions import when
from pyspark.sql.functions import col
from pyspark.sql.window import Window
from pyspark.sql.types import *


spark = SparkSession.builder.appName("SensorJOB").master("local[*]").getOrCreate()



def print_each_line(eachLine):
    print eachLine
    return



csv_df = spark.read.option("header", "true").csv('/Users/dharshekthvel/ac/ddata/realdatav3.csv')


window_specification=Window.orderBy("Sensor")


df_with_previous_row=csv_df.withColumn("previous_row_data", lag("data").over(window_specification)) \
                           .withColumn("previous_row_timestamp", lag("timestamp").over(window_specification))

df_with_difference = df_with_previous_row.withColumn("date_difference_start", when(col("data")-col("previous_row_data") < 0, col("timestamp")))\
                                         .withColumn("date_difference_end", when(col("data")-col("previous_row_data") > 0, col("timestamp")))\
                                         .withColumn("date_difference", when(col("data")-col("previous_row_data") != 0, col("timestamp"))
                                         .otherwise("0")).where("date_difference != '0'")\
                                         .withColumn("date_difference_next_row", lead("timestamp").over(window_specification))\
                                         .withColumnRenamed("date_difference", "start_date")\
                                         .withColumnRenamed("date_difference_next_row", "end_date")\
                                         .drop("previous_row_data", "previous_row_timestamp", "date_difference_start", "date_difference_end","timestamp")

df_with_difference.show(1000)

