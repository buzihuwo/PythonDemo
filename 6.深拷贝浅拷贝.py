#!/usr/bin/env python3
# -*- coding: utf-8 -*-



a=[1,2,3]
b=a
print(id(a)) #id()是才看内存的地址
print(id(b))


# 浅拷贝  里面的元素相同，但是内存地址不是同一个

a=[1,2,3]
b=[11,22,33]
c=[111,222,333]
list001=[a,b,c]
print(id(list001))
list002=list001[:] #切片  相当于创建一个新的参数
print(id(list002)) 



# 深拷贝  
import copy
list003=copy.deepcopy(list001)
print(id(list003))