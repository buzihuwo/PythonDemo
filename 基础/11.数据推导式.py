#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 求100到999中的水仙花数   如153   百位1**3+十位5**3+个位3**3等于自己
list0011=[i for i in range(100,1000) if i==(i//100)**3+(i%100//10)**3+(i%10)**3]
print(list0011) 


# 列表推导式
print('列表推导式'+'-'*20)
list003=['joe','susan','jack','tom']
name=[i for i in list003 if len(i)>=4]
print(name)

# 列表嵌套循环 推导式
print('列表嵌套循环 推导式'+'-'*20)
list001=[['joe','susan','jack','tom'],['joe1','susan1','jack1','tom1']]
list002=[n for i in list001 for n in i]
print(list002)


# 元组推导式
print('元组推导式'+'-'*20)
tuple001=('joe','susan','jack','tom')
tuplename=(i for i in tuple001  if len(i)>=4)
print(tuple(tuplename))

# 字典推到式  
'''
enumerate一个索引序列  
如  0 joe
    1 susan
    2 jack
'''
print('字典推到式'+'-'*20)
dict001 ={k:v for k,v in enumerate(list003)}
print(dict001)