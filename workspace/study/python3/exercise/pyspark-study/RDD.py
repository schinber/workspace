# coding:utf-8
import findspark

findspark.init()
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
import math

# import cassandra

appName = "jhl_spark_1"  # 你的应用程序名称
master = "local"  # 设置单机
conf = SparkConf().setAppName(appName).setMaster(master)  # 配置SparkContext
sc = SparkContext(conf=conf)

data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data, numSlices=10)
print(distData.collect())
