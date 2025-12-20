# coding:utf-8
import pandas as pd
import numpy as np

# 创建DataFrame对象
df = pd.DataFrame([1, 2, 3, 4, 5], columns=['cols'], index=['a', 'b', 'c', 'd', 'e'])
print
"df1"
print
df
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['col1', 'col2', 'col3'], index=['a', 'b'])
print
"df2:"
print
df2
print
type(df2)
df3 = pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['col1', 'col2'], index=['a', 'b'])
print
"df3"
print
df3
print
type(df3)

df4 = pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]}, index=['a', 'b'])
print
df4
print
"*" * 100
print
df2.index
print
df2.columns
# print df2.loc['a']
print
df2.loc[['a']]
print
df2.iloc[0]
print
df2.loc[['a', 'b']]
print
"*" * 100
data4 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df4 = pd.DataFrame(data4)
print
df4
print
"df4 第0行数据："
print
df4.loc[[0]][['c']]
print
"Series"
from pandas import Series

obj = Series([2, 3, 4, 5])
print
obj
print
obj[3]
