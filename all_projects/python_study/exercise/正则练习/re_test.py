"""
正则练习测试
"""
import re

# 示例1
bytes("acb")

xx = '{"abc", "cdd"}'
pattern = re.compile(r'\"(.*?)\"')
result = pattern.findall(xx)
print(result)

# 示例2
yy = "{'abcxx', 'cdd'}"
pattern = re.compile(r"\'(.*?)\'")
result = pattern.findall(yy)
print(result)