# coding:utf-8

d = dict(a=1, b=2, c=3)
# print d[:1] # 字典没有切片 和 通过索引获取的方法
a = (1, 2, 3)
print(type(a))

print(a[:1])

# setdefault()

d1 = {"a": 1, "b": 2}
d1.setdefault("c", 123)
print(d1)

exit()
