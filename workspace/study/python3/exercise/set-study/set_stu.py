# coding:utf-8

a = set()
a.add(1)
print(a)

a.add("a")

print(a)

b = a.pop()
print(b)

print("*" * 100)
set1 = set([9, 4, 5, 2, 6, 7, 1, 8])
print(set1)
print(set1.pop())
print(set1)
# 结果:
# {1, 2, 4, 5, 6, 7, 8, 9}
# 1
# {2, 4, 5, 6, 7, 8, 9}

set1 = set((6, 3, 1, 7, 2, 9, 8, 0))
print(set1)
print(set1.pop())
print(set1)
# 结果:
# {0, 1, 2, 3, 6, 7, 8, 9}
# 0
# {1, 2, 3, 6, 7, 8, 9}
