from pyspark import SparkContext

import os


sc = SparkContext()
lines = sc.parallelize(['first','spark','code'])


# If you get a winutils.exe exception then add the below line
# Put the winutils.exe in the bin folder inside D:/ac/winutils/bin
os.environ['HADOOP_HOME'] = "D:/ac/winutils/"

# print (lines.first())
#
for each in lines.take(10):
    print each
