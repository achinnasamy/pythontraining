
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.functions import lag
from pyspark.sql.functions import when
from pyspark.sql.functions import col
from pyspark.sql.window import Window


spark = SparkSession.builder.appName("SensorJOB").master("local[*]").getOrCreate()



def print_each_line(eachLine):
    print eachLine
    return

csv_df = spark.read.option("header", "true").csv('/Users/dharshekthvel/ac/ddata/realdata.csv')


sorted_df = csv_df   .groupBy("Mnemonic", "Sensor", "data", "timestamp")\
                     .max()\
                     .sort("Mnemonic", "data", )


window_specification=Window.orderBy("Mnemonic")


df_with_previous_row=sorted_df.withColumn("previous_row_data", lag("data").over(window_specification))
df_with_difference = df_with_previous_row.withColumn("date_difference_start", when(col("data")-col("previous_row_data") < 0, col("timestamp")))\
                                         .withColumn("date_difference_end", when(col("data")-col("previous_row_data") > 0, col("timestamp")))

dropped_data_frame = df_with_difference.drop("previous_row_data")

dropped_data_frame.registerTempTable("SENSOR_TABLE")

#dropped_data_frame.na.seq()

dropped_data_frame.show(1000)

