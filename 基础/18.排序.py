#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字典排序
dic={'a':1,'c':2,'b':3}
print(dic.items())
# 通过内置函数sorted进行排序
dic=sorted(dic.items(),key=lambda x: x[1],reverse=True) #内置函数有返回值  reverse=True是倒序   
print({k:v  for k,v in dic})#字段推导式


# 列表排序
list001 =[{'name':'joe','age':18},{'name':'susan','age':19},{'name':'tom','age':17}]
lists=sorted(list001,key=lambda x: x['name'],reverse=True)
print(lists)

# 一元列表排序
a=[3,1,2]
a.sort()
print(a) 



# 元组排序
tuples=(3,2,5,4)
tuple001=sorted(list(tuples))
print(tuple(tuple001))