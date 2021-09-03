# coding:utf-8
import findspark

findspark.init()
from pyspark.sql.session import SparkSession

# from pyspark import SparkContext, SparkConf

# appName = "jhl_spark_1"  # 你的应用程序名称
# master = "local"  # 设置单机
# conf = SparkConf().setAppName(appName).setMaster(master)  # 配置SparkContext
# sc = SparkContext(conf=conf)

spark = SparkSession \
    .builder \
    .appName("test") \
    .config("spark.some.config.option", "一些设置") \
    .getOrCreate()

sc = spark.sparkContext
# df = spark.read.csv("file://d:/20181021105223_34042.csv", header=True,
#                     sep="|")  # 读取文件
# print(df.collect())

rdd = sc.parallelize([1, 2, 3, 4], 2)


def f(iterator): yield sum(iterator)


res = rdd.mapPartitions(f).collect()
print(res)
from operator import add

sorted()
