from pyspark.conf import SparkConf
from pyspark.context import SparkContext

from sparkpackage.sales_dto import SalesDTO


def print_lines(line):
    print line.product_name


config = SparkConf()
config.setAppName("CSVReaderJOB")
config.setMaster("local[*]")


context = SparkContext(conf=config)


textFileRDD = context.textFile('/home/dharshekthvel/ac/code/scalatrainingintellij/data/sales.csv')

# Broadcast
# amazon_product = context.broadcast(SalesDTO("AMAZON_PRODUCT"))
# mappedRDD = textFileRDD.map(lambda x : amazon_product.value)
# mappedRDD.foreach(lambda x : print_lines(x))

# Accumulator

context.accumulator()

