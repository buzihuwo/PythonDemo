#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
open('文件名','打开的模式')
r:只读的方式打开，如果文集不存在会提示错误
w：只写的方式打开，如果文件存在则覆盖，不存在创建
a:打开一个文件进行追加内容，如果存在则打开，不存在则创建新的文件，不存在则新建的文件

r+：读写，会将文件的指针调到文件的头部
w+：读写，文件不存在直接创建，存在覆盖源文件
a+：追加读写，会将文件的指针调到文件的末尾
'''


# 读 第一种   
# 打开文件
f=open('基础\\test.txt','r',encoding='utf-8') 
#  读取文件内容
# print(f.read()) 

print(f.readlines()) #按行来读取
#  关闭文件
f.close()

# 第二种   不需要close，它会自己关闭
with open('基础\\test.txt','r',encoding='utf-8') as f:
    print(f.read())


# 写  
f1=open('基础\\test.txt','a',encoding='utf-8')
f1.write('写入操作')
f1.close()


'''
文件与文件夹的操作
'''
import os
# 获取当前路径
print(os.getcwd())

# 列出当前或指定目录下的文件
print(os.listdir())

# 判断是否是一个文件
print(os.path.isfile('基础\\demo.txt'))

# 判断文件是否存在
print(os.path.exists('基础\\demo.txt'))

#重命名文件
# os.rename('基础\\demo.txt','基础\\demo1.txt')

#删除文件
# os.remove('基础\\demo.txt')

# 创建文件夹
# os.mkdir('基础\\demo')

#删除文件夹
# os.rmdir('基础\\demo')