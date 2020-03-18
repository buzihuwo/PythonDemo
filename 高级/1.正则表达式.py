#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
正则表达式规则

^开始
+匹配一个或者多个
$结束
'''


import re


'''
finfall  以列表形式返回匹配到的字符串
'''
pattern=re.compile('[a-zA-Z]+')#任意长度匹配英文字母
str1='123asdf43YUGuyg53jkhkj42534klhk6546'#会匹配整个字符串，蒋符号规则的保存在列表中
result=pattern.findall(str1)
print(result)#返回一个符合的列表
