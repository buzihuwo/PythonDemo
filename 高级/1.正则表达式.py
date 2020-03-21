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



'''
finditer  可以返回完整的正则匹配结果，以及分组的匹配结果
'''
pattern=re.compile('([a-z])[a-z]([a-z])')#任意长度匹配英文字母
str1='123asdf43YUGuyg53jkhkj42534klhk6546'#会匹配整个字符串，蒋符号规则的保存在列表中
result=pattern.finditer(str1) # 返回一个迭代器
print([n.group() for n in result]) #返回一个match，使用group返回完整的匹配结果


'''
split  分割 
'''

print(re.split('\d','one1two2three3fotr'))
print(re.split(',','one,two,three,fotr'))  #或者用\W


'''
sub 替换
'''
print(re.sub(',','-','one,two,three,fotr')) #第一个参数是要匹配的值 第二个是要替换的值 第三个是需要被替换的字符串
print(re.subn(',','-','one,two,three,fotr')) # 返回替换后的结果以及次数


'''
引用分组
'''

string ='hello 123,world 321'
pattern1=re.compile('(\w+) (\d+)')
print ([i.group() for i in pattern1.finditer(string)])
print(pattern1.sub(r'\2 \1',string))
print(pattern1.sub(r'\2****\1',string))


'''
贪婪和非贪婪
贪婪：在整个表达式匹配成功的前提下，尽可能的多的匹配
非贪婪：在整个表达式匹配成功的前提下，尽可能的少的匹配
'''
str1 ='aaa<p>hello</p>bbb<p>world</p>ccc'
patt1=re.compile('<p>.*</p>') #.匹配任意字符串*0~无限次
print('%s%s%s'%('-'*10,'贪婪','-'*10))
print(patt1.findall(str1))#贪婪
print('%s%s%s'%('-'*10,'非贪婪','-'*10))
patt1=re.compile('<p>.*?</p>') 
print(patt1.findall(str1))#贪婪

'''
匹配中文
'''
str3='你好,hello,帅哥'
patt3=re.compile('[\u4e00-\u9fa5]+')
print(patt3.findall(str3))

'''
练习
'''
stra='13955668877'
patt=re.compile('(\d[3])\d[4](\d[4])')
print('%s%s%s'%('-'*10,'练习','-'*10))
print([i.group() for i in patt.finditer(stra)])