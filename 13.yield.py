#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
yield和return的区别 
yield返回对象还会执行下面的代码 yield是生成器 生成一个迭代器  返回一个iterable迭代对象  yield可以返回多次
return是返回对象不会执行下面的代码  return只能返回一次
'''
def getNum(n):
    i=0
    while i<=n:
        yield i
        i+=1

# yield的函数会变成generator的生成器
a=getNum(5)

# 两种取值方式  手动
print(next(a))
print(next(a))

# 循环取 
for i in a:
    print(i)

# generator ()生成器  不是元组推导式
b = (x for x in range(10000))
print(b)
print(next(b))
print(next(b))


print('-'*20)
def gen():
    i=0
    while i<5:
        temp= yield i #不是赋值操作
        # 使用yield之后是一个生成器
        print(temp) #因为yield之后返回结果到调用者的地方， 暂停运行， 赋值操作没有运行
        i+=1
g=gen()
print(next(g))
# print(next(g))
print(g.send('我是a')) #可以将值发送到上一次yield的地方
