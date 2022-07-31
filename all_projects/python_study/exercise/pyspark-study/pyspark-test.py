import os
import findspark

findspark.init()
# os.environ['JAVA_HOME'] = r"E:\Program Files\Java\jdk1.8.0_131"
os.environ['JAVA_HOME'] = r"/usr/local/java/jdk1.8.0_181"
os.environ['SPARK_HOME'] = "/home/tianxinbo/deploy/spark-2.2.0-bin-hadoop2.7"
from pyspark.conf import SparkConf
from pyspark.context import SparkContext

conf = SparkConf().setMaster("spark://master:7077").setAppName("test")
sc = SparkContext(conf=conf)
print(sc)

# from pyspark import SparkContext
# from pyspark import SparkConf
# # os.environ['SPARK_HOME'] = r"F:\big_data\spark-2.3.3-bin-without-hadoop"
# os.environ['SPARK_HOME'] = r"F:\pyspark-study\spark-2.4.4-bin-hadoop2.7"
# # os.environ["HADOOP_HOME"] = r"F:\big_data\hadoop-2.6.5"
#
# print(0)
# conf = SparkConf().setMaster("spark://spark_cluster:7077").setAppName("test")
# sc = SparkContext(conf=conf)
# print(1)
# logData = sc.textFile("file:///opt/spark-2.3.3-bin-without-hadoop/README.md").cache()
# print(2)
# print("num of a",logData)
# sc.stop()
