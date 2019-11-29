
from pyspark import SparkConf
from pyspark import SparkContext

def filterNeededRecords(line):
    res = line.split(",")
    if(len(res) > 9):
        return line
    else:
        return ""

sparkconfig = SparkConf()
sparkconfig.setMaster("local[*]")
sparkconfig.setAppName("AlienDisneyJOB")


#
#
#
#
def splitRecords(line):

    line_array = line.split(',')

    initial_index = 0
    edge_index = 9
    line_array_length = len(line_array)
    iterations = line_array_length / 8

    for each in range(iterations):

        #description_column = line_array[edge_index - 1]
        #print description_column[-7:]


        each_line_array = line_array[initial_index : edge_index]
        print each_line_array


        initial_index = edge_index

        if (edge_index <= line_array_length):
            edge_index = edge_index + 8
        else:
            edge_index = line_array_length

    return line

def print_each_line(eachLine):
    print eachLine
    return


sparkcontext = SparkContext(conf= sparkconfig)

csvRDD = sparkcontext.textFile('/Users/dharshekthvel/ac/ddata/alien.csv')

mappedRDD = csvRDD.map(lambda f: filterNeededRecords(f))
reckoned_records = mappedRDD.filter(lambda x: x != "")

reckoned_records.map(splitRecords).collect()

#reckoned_records.foreach(print_each_line)



