# 1.简单小例子
f = lambda x, y, z: x + y + z
print(f(1, 2, 3))

# 2.支持默认值参数
g = lambda x, y=1, z=2: x + y + z
print(g(15, 16, 25))

from collections import OrderedDic
