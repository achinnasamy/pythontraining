from pyspark import SparkConf, SQLContext
from pyspark import SparkContext


sparkconfig = SparkConf()
sparkconfig.setMaster("local[*]")
sparkconfig.setAppName("AggregateANDSortByKeyJob")

sparkcontext = SparkContext(conf= sparkconfig)

textFileRDD = sparkcontext.textFile("../data/trip_1.csv")
print("File type => ",type(textFileRDD))
print("Row Count => ",textFileRDD.count())


linesWithCommit = textFileRDD.filter(lambda line: "Hamilton Garage" in line)
print("Hamilton Garage Point:")
print("     Count => ",linesWithCommit.count())



print("AGGREGATEBYKEY")
filtered_rows = textFileRDD.map(lambda line: line.split(","))
# filtered_rows = textFileRDD.filter(lambda line: "Hamilton Garage" in line).map(lambda line: line.split(","))
result1=filtered_rows.map(lambda n: (str(n[11]), 1)).aggregateByKey(0, lambda k, v: int(v) + k,lambda v, k: k + v).collect()
print(result1)


print("SORTBYKEY")
print("Normal Order")
result2=filtered_rows.map (lambda n:  (str(n[11]),1 ) ).aggregateByKey(0, lambda k, v: int(v) + k,lambda v, k: k + v).sortByKey().collect()
print(result2)
print("Reverse Order")
result3=filtered_rows.map (lambda n:  (str(n[11]),1 ) ).aggregateByKey(0, lambda k, v: int(v) + k,lambda v, k: k + v).sortByKey(False).collect()
print(result3)

