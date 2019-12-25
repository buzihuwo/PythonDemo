#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 元组是小括号()，元组不可修改  列表是方括号[]
tuple001=(1,2,3,4)
print(tuple001)

# 元组的长度
print(len(tuple001))


# 删除 del  彻底删除
del tuple001

# list,tuple 互转
list001=['a','b','c']
print('-'*20+'list转tuple'+'-'*20)
print(type(list001))
tuple001=tuple(list001)
print(type(tuple001))
print('-'*20+'tuple转list'+'-'*20)
list002= list(tuple001)
print(type(list002))