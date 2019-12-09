#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list001 =['jack','jane','joe','black']
print(list001[2])

list002 =['jack','jane',['zzzzz','joe'],'black']
print(list002[2][0])




# 查询  in   not in
print('-'*20+'查询  in'+'-'*20)
print(['zzzzz','joe'] in list002)
print('-'*20+'查询  not in'+'-'*20)
print('jane' not in list002)


# 修改
print('-'*20+'修改'+'-'*20)
print(list002)
list002[0]='lili'
print(list002)

#  追加  最后面追加
print('-'*20+'追加append'+'-'*20)
list002.append('susan')
print(list002)

#  指定下标追加
print('-'*20+'指定下标追加insert'+'-'*20)
list002.insert(1,'susan')
print(list002)

# 删除 pop  默认删除最后一个  并且返回删除的元素 也可以通过下标来删除
print('-'*20+'删除 pop'+'-'*20)
list003= ['jack','jane','joe','black']
print(list003)
# print(list003.pop()) 
# print(list003)

# del 删除后就能访问
# del list003[0]
# print(list003)


# remove 不需要指定下标  通过元素的值来删除
list003.remove('joe')
print(list003)


# 列表追加列表  extend
print('-'*20+'列表追加列表  extend'+'-'*20)
list004=['00411','00422','00433']
list005=['00511','00522','00533']
list004.extend(list005)
print(list004)