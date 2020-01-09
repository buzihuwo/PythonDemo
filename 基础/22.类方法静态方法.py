#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
静态方法和类方法推荐用类名调用
'''

class person():
    '''
    这是一个人类的类
    '''
    # 实例属性通过构造方法来声明
    #self不是关键字，代表当前对象
    def __init__(self,name,age,sex):#构造方法
        # 构造方法不需要调用，它会在实例化的时候自动调用
        print('我是构造方法，在实例化的时候调用')
        self.name=name #通过self 创建实例属性，并赋值
        self.age=age
        self.sex=sex

    # 创建普通方法
    def getName(self):
        print('我的名字叫%s'%self.name)#在方法里面使用实例属性
    country='中国'#类属性

# 创建一个静态方法
    @staticmethod
    def getA():#不需要传入实例
        #静态方法不能用实例属性self
        #静态方法只能访问类属性
        print('静态方法我的名字叫%s'%person.country)

# 创建一个类方法
    @classmethod
    #类方法不能用实例属性self
    #类方法只能访问类属性
    def aa(cls): #cls是class简写 也不是关键字 
        print('类方法我的名字叫%s'%cls.country)
    6


person.getA()
person.aa()   
