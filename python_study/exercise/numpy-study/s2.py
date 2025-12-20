# coding:utf-8

import numpy as np

x = np.empty([3, 2], dtype=int)
print
x

print
np.zeros(5, dtype=int)
print
np.ones(6, dtype=int)

s = 'Hello World'
a = np.frombuffer(s, dtype='S1')
print
a

c = list(a)
print
c
print
type(c)

list = range(5)

it = iter(list)
# 使用迭代器创建 ndarray
x = np.fromiter(list, dtype=float)
print
x

print
np.arange(1, 10, 2, dtype=float)

print
np.linspace(1, 100, num=50, endpoint=True)
