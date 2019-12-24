#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定义函数
def Pname():
    print('大家好我是大可爱')

# 调用函数
Pname()

# 必备参数  name,address
def getInfo(name,address):
    print('大家好我叫%s,我来自%s'%(name,address))
getInfo('刘德华','香港')

# 关键字参数
getInfo(address='地球',name='jeff')

# 参数的默认值  address
def aName(name,address='地球上'):
    print('大家好我是渣渣辉，我的名字是%s,家在%s'%(name,address))
aName('张家辉')

# 不定长参数  
'''
*args  带一颗*的参数  是就收所以未命名的参数
**args2  带一颗**的参数  是就收所以关键字参数
'''
def bName(name,address,*args,**args2):
    print('大家好我是渣渣辉，我的名字是%s,家在%s'%(name,address))
    print(args) #args  是一个元组
    print(args2) #args2  是一个字典
'''
 只要是没定义的如abc都会进args
 只要是关键字参数的如age=18,sex='男'都会进args2
'''
bName('张家辉','香港','a','b','c',age=18,sex='男')  


# 返回函数
def max(x,y):
    if x>y:
        return x
    else:
        return y
print(max(1,2))


# 返回多个函数
def num(x,y):
    return x,y

# 一个变量接受
num11=num(22,33)
print(num11)
# 多个变量接受
num2,num3=num(22,33)
print('第一个数%s,第二个数%s'%(num2,num3))

