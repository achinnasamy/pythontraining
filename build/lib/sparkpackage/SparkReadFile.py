

from pyspark import SparkContext
from pyspark.conf import SparkConf

config = SparkConf()

config.setAppName("SPARK_READ_FILE_JOB")
config.setMaster("local[*]")
sc = SparkContext(conf=config)


def print_each_line(eachLine):
    print eachLine
    return

textFileRDD = sc.textFile("/home/dharshekthvel/history_1.txt")
mappedRDD = textFileRDD.map(lambda x : len(x))


mappedRDD.foreach(print_each_line)
#
# for line in mappedRDD.take(100):
#     print line



# data = textFileRDD.collect()
#
# for each in data:
#     print each



