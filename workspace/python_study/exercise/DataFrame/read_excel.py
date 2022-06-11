# coding:utf-8
import pandas as pd
import numpy as np

path = r'D:/excel/school.xlsx'
try:
    res = pd.read_excel(path, sheet_name='Sheet1')
    # , index_col=None,usecols=['task_id', 'name', 'age', 'email'])
except Exception as e:
    print
    e
# print res
a = np.array(res)
# print a
# print type(a)
b = a.tolist()

# print b


# for x in b:
#     print x
# print
print[{"task_id": x[0], "name": x[1], "age": x[2], "email": x[3]}
for x in b]

print
# print map(lambda x: {"task_id": x[0], "name": x[1], "age": x[2], "email": x[3]}, b)
