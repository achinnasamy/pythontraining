from __future__ import print_function
from pyspark.conf import SparkConf
from pyspark.context import SparkContext




config = SparkConf()
config.setAppName("SPARK_WORD_COUNT_JOB")
config.setMaster("local[*]")

sc = SparkContext(conf=config)
sc.setLogLevel("info")
text_file_rdd = sc.textFile("/home/dharshekthvel/history_1.txt")
flat_mapped_rdd=text_file_rdd.flatMap(lambda each: each.split(' '))
mapped_rdd = flat_mapped_rdd.map(lambda each: (each,1))
mapped_rdd.reduceByKey(lambda x,y: x+y)\
    .foreach(print)
