#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 
迭代器就是 for in 遍历得对象都可以叫做迭代器 Iterable
list string dict
可以被next()函数调用的并不断返回下一个值的对象叫做迭代器:iterator
凡是可以用作于next()函数的对象都是iterator
'''

list001=[x for x in range(0,6)]
# print(next(list001))  list001不是迭代器所以无法调用 next
# 通过iter()将一根可迭代对象变成迭代器
a =iter(list001)
print(a)
print(next(a))
print(next(a))
print(next(a)) 



# 练习
# 判断类型用的 
isinstance(a,str)

def getList(*args):
    list002=[i for i in args]
    return list002
print(getList(1,3,2,4))

def getSum(*args):
    a=0
    for i in args:
        a+=i
    return a
print(getSum(2,3,4,2,1,3,1,2))