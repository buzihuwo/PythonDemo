#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list001=['joe','susan','jack','tom']

# for a in list001:
#     print(a)

#  遍历字典
dict001= {'张三':['上海','北京','深圳'],'李四':['张家界','九寨沟','鼓浪屿']}
for a in dict001:
    print(dict001[a])


list001=['joe','susan','jack','tom']
for a in list001:
    if(a=='李四'):
        continue
    print(a)