#!/usr/bin/env python3
# -*- coding: utf-8 -*-


''''''
'''
import 模块名[,模块名].....
导入整个模块
通过 模块名.方法名调用
'''

# import time
# print('开始')
# time.sleep(5)
# print('结束')


#给导入的模块取别名
import time as t
print('开始')
t.sleep(5)
print('结束')



'''
from 模块名 import 函数名
从指定的模块中导入指定的部分
'''

# from time import sleep
# import time
# print('开始')
# sleep(5)
# print('结束')


'''
from 模块名 import *
导入模块中的所有内容
'''
# from math import *
# print(ceil(1.1))#向上取整
# print(floor(1.1))#向下取整