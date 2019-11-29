
from __future__ import print_function
from pyspark.conf import SparkConf
from pyspark.context import SparkContext

config = SparkConf()
config.setMaster("local[*]")
config.setAppName("DATA_JOB")


sc = SparkContext(conf=config)

# Transformation
textFileRDD = sc.textFile("/Users/dharshekthvel/ac/data/auth.csv")

#type(textFileRDD)


textFileRDD.foreach(lambda each : print(each))

sc.stop()


