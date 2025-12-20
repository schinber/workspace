import os
import sys
import re

try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print("Successfully imported Spark Modules")
except ImportError as e:
    print("Can not import Spark Modules", e)
