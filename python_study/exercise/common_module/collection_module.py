# coding:utf-8

from collections import Counter, OrderedDict, deque

# nums = set-study([1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2])
#
# print heapq.nlargest(3, nums)
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

# d = OrderedDict()
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od)
od.items()

d = deque([1, 2, 3])
print(d)

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in p13?')
md5.hexdigest()

print("*" * 100)
a = OrderedDict([('z', 1), ('y', 2), ('x', 3)])
print(a)

for i in a.items():
    print(i)

b = {"a": 1, "c": 3, "b": 2}
for k, v in b.items():
    print(k, v)
