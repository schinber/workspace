import re

# 示例1：匹配成功（字符串开头符合正则）
text = "Python 3.10+ supports regex"
pattern = r"Python"  # 匹配开头的 "Python"
result = re.match(pattern, text)
print(result)  # 输出：<re.Match object; span=(0, 6), match='Python'>
