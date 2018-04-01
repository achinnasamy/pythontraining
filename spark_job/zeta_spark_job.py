from pyspark import SparkConf
from pyspark import SparkContext
zeta_spark_config=SparkConf()
zeta_spark_config.setMaster("local[*]")
zeta_spark_config.setAppName("Zeta_Spark_job")
def print_csv_file(eachline):
    print eachline

zeta_spark_context=SparkContext(conf=zeta_spark_config)
zeta_textfilerdd=zeta_spark_context.textFile("/home/dharshekthvel/Desktop/ac/code/scalatrainingintellij/data/auth.csv")
zeta_textfilerdd.foreach(print_csv_file)
#zeta_textfilerdd.mapPartitions(print_csv_file).collect()
#zeta_textfilerdd.print_csv_file().count()

#print zeta_textfilerdd.collect()

#zeta_textfilerdd.count()

print zeta_textfilerdd.first()


#zeta_textfilerdd=zeta_spark_context.
'''print type(zeta_textfilerdd)

print type(zeta_spark_config)

print type(zeta_spark_context)
'''