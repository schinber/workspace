# coding:utf-8

# 1.连接spark
import os

import pandas as pd
import numpy as np
# import findspark
# findspark.init()
os.environ['PYSPARK_PYTHON'] = r"D:\Python39\python.exe"
# os.environ['JAVA_HOME'] = r"E:\Program Files (x86)\Java"
# os.environ['SPARK_HOME'] = r'F:\SPARK\spark-2.3.2-bin-hadoop2.7'
from pyspark.sql import SparkSession
import platform
# if platform.version() == "3.7.3":

spark = SparkSession.builder.appName('tianxinbo').getOrCreate()

# 2. 创建dataframe
# 2.1. 从变量创建
stringCSVRDD = spark.sparkContext.parallelize([
    (123, "Katie", 19, "brown"),
    (234, "Michael", 22, "green"),
    (345, "Simone", 23, "blue")
])

# 指定模式, StructField(name,dataType,nullable)
# 其中：
# name: 该字段的名字，
# dataType：该字段的数据类型，
# nullable: 指示该字段的值是否为空
from pyspark.sql.types import StructType, StructField, LongType, StringType  # 导入类型

schema = StructType([
    StructField("id", LongType(), True),
    StructField("name", StringType(), True),
    StructField("age", LongType(), True),
    StructField("eyeColor", StringType(), True)
])

# 对RDD应用该模式并且创建DataFrame
swimmers = spark.createDataFrame(stringCSVRDD, schema)
swimmers.registerTempTable("swimmers")
# 查看DataFrame的行数
print(swimmers.count())

# 2.2. 从变量创建
# 使用自动类型推断的方式创建dataframe
data = [(123, "Katie", 19, "brown"),
        (234, "Michael", 22, "green"),
        (345, "Simone", 23, "blue")]
df = spark.createDataFrame(data, schema=['id', 'name', 'age', 'eyccolor'])
df.show()
df.count()

# 2.3. 读取json
file = r"F:\SPARK\spark-2.3.2-bin-hadoop2.7\examples\src\main\resources\people.json"
df = spark.read.json(file)
df.show()

# 2.4. 读取csv
# 先创建csv文件


df = pd.DataFrame(np.random.rand(5, 5), columns=['a', 'b', 'c', 'd', 'e']). \
    applymap(lambda x: int(x * 10))
file = r"F:\SPARK\spark-2.3.2-bin-hadoop2.7\examples\src\main\resources\random.csv"
df.to_csv(file, index=False)

# 再读取csv文件
monthlySales = spark.read.csv(file, header=True, inferSchema=True)
monthlySales.show()

# 2.5.读取MySQL

# 此时需要将mysql-jar驱动放到spark-2.2.0-bin-hadoop2.7\jars下面
# 单机环境可行，集群环境不行
# 重新执行
df = spark.read.format('jdbc').options(
    url='jdbc:mysql://127.0.0.1',
    dbtable='mysql.db',
    user='root',
    password='root'
).load()
df.show()
# 也可以传入SQL语句
sql = "(select * from mysql.db where db='wp230') t"
df = spark.read.format('jdbc').options(
    url='jdbc:mysql://127.0.0.1',
    dbtable=sql,
    user='root',
    password='root'
).load()
df.show()

# 2.6. 从pandas.dataframe创建
# 如果不指定schema则用pandas的列名
df = pd.DataFrame(np.random.random((4, 4)))

# 2.7. 从列式存储的parquet读取
# 读取example下面的parquet文件
file = r"D:\apps\spark-2.2.0-bin-hadoop2.7\examples\src\main\resources\users.parquet"
df = spark.read.parquet(file)
df.show()
# 2.8. 从hive读取

spark = SparkSession \
    .builder \
    .enableHiveSupport() \
    .master("172.31.100.170:7077") \
    .appName("my_first_app_name") \
    .getOrCreate()
df = spark.sql("select * from hive_tb_name")
df.show()
