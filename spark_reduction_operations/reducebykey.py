from pyspark import SparkConf, SQLContext
from pyspark import SparkContext


sparkconfig = SparkConf()
sparkconfig.setMaster("local[8]")
sparkconfig.setAppName("SparkCSVJOB")

sparkcontext = SparkContext(conf= sparkconfig)

textFileRDD = sparkcontext.textFile("C:\\Users\\Adsausere6\\Documents\\Sara\\Bigdata\\data\\trip_1.csv")
print("REDUCEBYKEY")
# filtered_rows = textFileRDD.filter(lambda line: "Hamilton Garage" in line).map(lambda line: line.split(","))
filtered_rows = textFileRDD.map(lambda line: line.split(","))
result=filtered_rows.map(lambda n:  (str(n[11]), 1 ) ).reduceByKey(lambda v1,v2: v1 + v2).collect()
print(result)