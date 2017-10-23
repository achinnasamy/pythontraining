


from pyspark import SparkConf
from pyspark import SparkContext

from sparkpackage.auth_carrier import AuthCarrier

spark_config = SparkConf()
spark_config.setMaster("local[*]")
spark_config.setAppName("SparkCSVJOB")

spark_context = SparkContext(conf= spark_config)



def print_each_line(eachLine):
    print eachLine.refid
    return

auth_carrier = AuthCarrier(1,2,999)
print auth_carrier.get_asacode()

auth_carrier.set_asacode("7009")
print auth_carrier.get_asacode()


text_file_rdd = spark_context.textFile("/home/dharshekthvel/ac/code/scalatrainingintellij/data/auth.csv")
text_file_rdd.map(lambda x: AuthCarrier(x.split(",")[0], x.split(",")[1], x.split(",")[2])).foreach(print_each_line)

'''  text_file_rdd.foreach(print_each_line) '''






