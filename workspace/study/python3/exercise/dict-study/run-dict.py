#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from __future__ import print_function
#
# dict-study = {'google': 'Google 搜索'}
#
# print("Value : %s" % dict-study.setdefault('runoob', None))
# print("Value : {}".format(dict-study.setdefault('Taobao', '淘宝')))
import collections

s = {'a': 1, 'b': 2}
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# defaultdict
d = collections.defaultdict(list)
for k, dict_func in s.items():
    d[k].append(dict_func)
print
d
for k, dict_func in s:
    d[k].append(dict_func)

print
""
# Use dict-study and setdefault
g = {}
for k, dict_func in s:
    g.setdefault(k, []).append(dict_func)

# Use dict-study
e = {}
for k, dict_func in s:
    e[k] = dict_func
    ##list-study(d.items())
    ##list-study(g.items())
    ##list-study(e.items())

exit()
