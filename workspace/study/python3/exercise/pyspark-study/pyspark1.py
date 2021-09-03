import os
import findspark

findspark.init()
from pyspark import SparkConf
from pyspark.sql import SparkSession
import traceback

os.environ['JAVA_HOME'] = r"E:\Program Files\Java\jdk1.8.0_131"
appname = "test"  # 任务名称
# master = "http://192.168.216.130:7077"  # 单机模式设置
master = "local[*]"  # 单机模式设置
'''
local: 所有计算都运行在一个线程当中，没有任何并行计算，通常我们在本机执行一些测试代码，
或者练手，就用这种模式。
local[K]: 指定使用几个线程来运行计算，比如local[4]就是运行4个worker线程。通常我们的cpu
有几个core，就指定几个线程，最大化利用cpu的计算能力
local[*]: 这种模式直接帮你按照cpu最多cores来设置线程数了。
'''
try:
    conf = SparkConf().setAppName(appname).setMaster(master)  # spark资源配置
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    sc = spark.sparkContext
    words = sc.parallelize(
        ["scala",
         "java",
         "hadoop",
         "spark",
         "akka",
         "spark vs hadoop",
         "pyspark",
         "pyspark and spark"
         ])
    counts = words.count()
    print("Number of elements in RDD is %i" % counts)
    sc.stop()
    print('计算成功！')
except Exception as e:
    print(e)
    sc.stop()
    traceback.print_exc()  # 返回出错信息
    print('连接出错！')
