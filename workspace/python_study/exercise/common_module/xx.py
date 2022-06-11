# coding:utf-8

x = {'banana': [2]}
y = {'banana': [10]}


def cc(x, y):
    # for k  in x:
    #     for ky in y:
    #         if k == ky:
    #             x[k].extend(vy)
    if x[0] == y[0]:
        x[1].append(y[1])
    return x


from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
import math

appName = "jhl_spark_1"  # 你的应用程序名称
master = "local"  # 设置单机
conf = SparkConf().setAppName(appName).setMaster(master)  # 配置SparkContext
sc = SparkContext(conf=conf)

data = [('banana', [{'banana': [2]}]), ('banana', [{'banana': [10]}]), ('bama', [{'bana': [10]}])]
distData = sc.parallelize(data, numSlices=10)
r = distData.reduce(cc)
print
r
