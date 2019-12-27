#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lambda

# 没有参数的的lambda
s=lambda : '哈哈哈哈'
print(s())


# 有参数的的lambda
a=lambda x: x*2
print(a(3))


# 有多个参数的的lambda
q=lambda x,y: x*y
print(q(3,4))

# 字典排序
dic={'a':1,'c':2,'b':3}
# 通过内置函数sorted进行排序
dic=sorted(dic.items(),key=lambda x: x[1],reverse=True) #内置函数有返回值  reverse=True是倒序   
print({k:v  for k,v in dic})#字段推导式