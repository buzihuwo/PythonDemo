#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# map 接受一个函数及多个集合序列，会根据提供的函数对指定的序列做映射，然后返回一个新的map对象
list001=[i for i in range(1,6)]
newlist= map(lambda x: x*2,list001)
print(list(newlist))#将map对象转换成list


list0011=[i for i in range(1,11,2)]
list0022=[i for i in range(2,11,2)]
newlist1=map(lambda  x,y: x*y,list0011,list0022)
print(list(newlist1))

# filter  用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的filter对象
newList0022= filter(lambda x: x>4,list0022)
print(list(newList0022))

# reduce 对于序列中的所有元素调用func进行数据合并操作，可以给定一个初始值
from functools import reduce
list2=[2,4,5,8,10]
print(reduce(lambda x,y: x+y,list2)) 
''' 
执行过程 第一次会把2给到x，4给到y，相加
第二次 拿到第一次的结果6给到x，5给到y,相加, 以此类推

如果有初始值  reduce(lambda x,y: x+y,list2,0) 0就是初始值，第一次0给x，2给y
'''


# 练习

name=['joe','susan','black','lili']
age=[18,19,20,21]
sex=['m','w','m','w']
# 格式化用户的英文名，要求首字母大写，其他字母小写
newName=map(lambda i: i.title(),name)
print(list(newName))

# 将用户英文名，年龄，性别三个集合的数据结合到一起，形成一个元组列表
newNAS=map(lambda n,a,s:(n,a,s),name,age,sex)
newNAS=list(newNAS)
print(newNAS)

# 过滤性别为男的用户
newSex=filter(lambda x:x[2] == 'm',newNAS)
newSex=list(newSex)
print(newSex) 

# 求性别为男的用户的平均年龄
print(reduce(lambda x,y: x+y[1],newSex,0)/len(newSex)) 