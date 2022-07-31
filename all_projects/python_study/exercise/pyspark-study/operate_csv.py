# coding:utf-8

from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext()
spark = SQLContext(sc)
dfcsv = spark.read.csv(r'D:\20181021105223_34042.csv', encoding='utf-8', header=True)
print(dfcsv)
