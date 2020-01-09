#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python允许多继承

class Animal():
    def __init__(self,name,food):
        self.name=name
        self.food=food

    def eat(self):
        print('%s爱吃%s'%(self.name,self.food))

#申明一个子类继承animal
class Dog(Animal): 
    def __init__(self,name,food,drink):
        # 加载父类构造函数
        super().__init__(name,food)# 第一种写法
        # Animal.__init__(self,name,food)# 第二种写法
        self.drink=drink

    def drinks(self):
        print('%s爱喝%s'%(self.name,self.drink))

# 重写父类方法
    def eat(self):
        print('%s特别爱吃%s'%(self.name,self.food))

dog1=Dog('金毛','骨头','可乐')
dog1.eat()
dog1.drinks()


# 多继承
class A():
    def a(self):
        print('我是A里面的a方法')

class B():
    def b(self):
        print('我是B里面的b方法')

class C():
    def a(self):
        print('我是C里面的a方法')
    def c(self):
        print('我是C里面的c方法')     

class D(A,B,C):
    def d(self):
        print('我是D里面的d方法')      

d1=D()
d1.a()
d1.b()
d1.c()
d1.d()