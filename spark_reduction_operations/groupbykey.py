from pyspark import SparkConf, SQLContext
from pyspark import SparkContext


sparkconfig = SparkConf()
sparkconfig.setMaster("local[8]")
sparkconfig.setAppName("SparkCSVJOB")

sparkcontext = SparkContext(conf= sparkconfig)

textFileRDD = sparkcontext.textFile("C:\\Users\\Adsausere6\\Documents\\Sara\\Bigdata\\data\\trip_1.csv")
print("GROUPBYKEY")
rows = textFileRDD.map(lambda line: line.split(","))
namesToCounties = rows.map(lambda n: (str(n[1]),str(n[11]) )).groupByKey()
result=namesToCounties.map(lambda x : {x[0]: list(x[1])}).collect()
print(result)