# coding:utf-8

import glob

# glob
p = glob.glob("D:/[1].txt")
print
p

# iglog

f = glob.iglob("D:/*.txt")
print
f
for i in f:
    print
    i
