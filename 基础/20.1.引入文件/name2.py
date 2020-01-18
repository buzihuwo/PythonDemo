#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
自定义模块
'''
import name 
print('%s%s%s'%('_'*10,'引入同级目录中的模块','_'*10))
name.a()

'''
跨模块引入
'''
from study import  test
print('%s%s%s'%('_'*10,'引入同级目录文件夹下的模块','_'*10))
test.a(3,6)



'''
跨模块引入
'''
import sys 
#查看路径

sys.path.append('../')#插入路径
print(sys.path)


'''
dir 
用于按模块名搜索模块定义，它返回一个字符串类型的存储过程
该列表列出了所有类型的名称：变量，模块,函数，等等
'''
print(dir())