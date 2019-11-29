
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import datetime
from pyspark.sql.functions import udf


def format_timestamp(ts):
    currentdata_time = ts[0:13]
    #print(currentdata_time)
    current_milliseconds = currentdata_time[-3:]
    #print(current_milliseconds)
    your_dt = datetime.datetime.fromtimestamp(int(currentdata_time) / 1000).strftime("%Y-%m-%d %H:%M:%S")  # using the local timezone
    return  your_dt+"."+current_milliseconds


format_timestamp_udf = udf(lambda x: format_timestamp(x))

spark = SparkSession.builder.appName("SensorJOB").master("local[*]").getOrCreate()


csv_df = spark.read.option("header", "true").csv('/Users/dharshekthvel/ac/ddata/only1sensor.csv')


data_df=csv_df  .withColumn("timestamp_difference", col("timestamp_end")-col("timestamp_start"))\
                .withColumn("timestamp_start_formatted", format_timestamp_udf(csv_df['timestamp_start']))

data_df.show()

