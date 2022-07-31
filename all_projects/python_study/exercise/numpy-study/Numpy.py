# coding:utf-8

from __future__ import print_function
import numpy as np

# x = np.array([[1, 2], [3, 4], [5, 6]])
# y = x[[0, 1, 2], [0, 1, 0]]
# print y
#
# print
#
# a = np.array(['a', 'b', 'c'])
# s = slice(0, 2, 1)
# print a[s]

x = np.arange(0, np.pi / 2, 0.1)
y = np.sin(x)
print("narray:", x, y)
