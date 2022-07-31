# coding:utf-8
import numpy as np

f = np.random.random((2, 3, 5))
print(f, f.shape)

# a = np.array([1, 2, 3])
# print a
b = np.array(['1', 'a'])
print
b
print
b.size
# c = np.array([1, 2, 3], ndmin=3)
# print c
# print
d = np.ones([1, 2])
print
d
print

test_numpy = np.linspace(0, 15, 17)
print
test_numpy
print
# print type(a)
# print a[1]
# print type(a[1])

# print type(a)
print
"*" * 100
##################################################################
# b = np.array([[1, 2], [3, 4]])
# print b
#
# print b[1][0]


# 最小维度
# c = np.array([1, 2, 3], ndmin=2)
# print c
# print c[0]

# 使用数组标量类型
dt = np.dtype(np.int32)
print
dt

# int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他。
dt1 = np.dtype('i8')
print
dt1
# 字符串i8相当于int64
print
"*" * 20 + "使用端记号" + "*" * 20
# 使用端记号
dt2 = np.dtype('>i4')
print
dt2

dt3 = np.dtype([('age', np.int8)])
print
dt3

# a = np.array([(10,), (20,), (30,)])
# print a
"""
# 文件名称可用于访问 age 列的内容
a1 = np.array([(10,), (20,), (30,)], dtype=dt3)
print a1['age']

# eg7:
student = np.dtype([("name", "S20"), ("age", "i1"), ("marks", "f4")])
print student

# eg8:
stu = np.dtype([("name", "S20"), ("age", "i1"), ("marks", "f4")])
s1 = np.array([("abc", 21, 50), ('xyz', 18, 75)], dtype=stu)
print "s1:", s1

# eg9:NumPy - 数组属性
# ndarray.shape
a = np.array([[1, 2, 3], [4, 5, 6]])
print "a:", a
print "a.shape:", a.shape

# NumPy 也提供了reshape函数来调整数组大小。
b = a.reshape(3, 2)
print "b" * 10
print b
print "b" * 10
# adarray.ndim这一数组属性返回数组的维数。
"""
a = np.arange(24)
print
a
b = a.reshape(4, 6)
print
"一维数组 ", a.ndim
print
b
#
# # 现在调整其大小
# b = a.reshape(2, 4, 3)
# print "b: ", b
# # numpy-study.itemsize
# # 这一数组属性返回数组中每个元素的字节单位长度。
# x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
# print "itemsize:", x.itemsize


# x =  [(1,2,3),(4,5)]
# a = np.array(x)
# print a
# print type(a)

x = np.array([1, 2, 3, 4, 51], dtype=np.int8)
print
x.itemsize
