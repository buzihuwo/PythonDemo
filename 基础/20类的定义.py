#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class person():
    '''
    这是一个人类的类
    '''
    # 实例属性通过构造方法来声明
    #self不是关键字，代表当前对象
    def __init__(self,name,age,sex,address):#构造方法
        # 构造方法不需要调用，它会在实例化的时候自动调用
        print('我是构造方法，在实例化的时候调用')
        self.name=name #通过self 创建实例属性，并赋值
        self.age=age
        self.sex=sex
        self.__address=address #__address是私有属性

    # 创建普通方法
    def getName(self):
        print('我的名字叫%s'%self.name)#在方法里面使用实例属性

    country='中国'#类属性


# 实例化对象
people01 = person('joe',19,'男','地球')   #在实例化的时候传递参数
people01.getName() #调用类里面的方法
print(people01.country)#调用类里面的类属性

# 内置内属性
print(people01.__dict__) # 会将实例对象的属性和值通过字典的形式返回
print(people01.__doc__) # 查看类的说明
print(__name__) # 返回类名  在当前文件运行会输出__main__  在别的文件引入会输出类名
print(person.__bases__) # 返回父类

# 通过内置方法访问属性
print(getattr(people01,'name'))
# 通过内置方法判断属性是否存在
print(hasattr(people01,'name'))
# 通过内置方法设置属性
setattr(people01,'name','susan')
print(getattr(people01,'name'))
# 通过内置方法删除属性
delattr(people01,'name')
print(hasattr(people01,'name'))


