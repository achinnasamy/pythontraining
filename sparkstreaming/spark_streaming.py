from pyspark.context import SparkContext
from pyspark.streaming.context import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

spark_context = SparkContext(appName='StreamingJOB', master='local[*]')
ssc = StreamingContext(spark_context, 10)

stream = ssc.socketTextStream('localhost', 7777)



stream.pprint()


ssc.start()
ssc.awaitTermination()
