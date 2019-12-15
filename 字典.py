#!/usr/bin/env python3
# -*- coding: utf-8 -*-
dict001={'name':'Jeff','age':18,'address':'上海'}
print(dict001['name'])

# 获取所有的key
print(dict001.keys())

# 获取所有的value
print(dict001.values())

# 修改
dict001['name']='jack'
print(dict001['name'])
# 添加
dict001['hobby']='足球'
print(dict001)
# 删除
del dict001['hobby']
print(dict001)
# 清空
dict001.clear()
print(dict001)

