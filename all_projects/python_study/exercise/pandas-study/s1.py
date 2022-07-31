# coding:utf-8
from functools import reduce

import numpy as np
import pandas as pd
import pyspark

a = np.array([1, 2, 3, 4])
s = pd.Series([1, 2, 3, 4])

print(s)
reduce()


# res = s.describe()
# print res
# print "*" * 100
#
# print res[0]


def a(x):
    return int(x * x)


r = map(a, s)
print(r)

print(type(r))
