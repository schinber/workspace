import re

xx = b"{'abcxx', 'cdd'}"
print(type(xx), xx)

xx_str = xx.decode()
print()
pattern = re.compile(r"\'(.*?)\'")
result = pattern.findall(xx_str)
print(result)
