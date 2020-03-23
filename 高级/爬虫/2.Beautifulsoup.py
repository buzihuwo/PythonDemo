#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
BeautifulSoup变成html对象
'''

from bs4 import BeautifulSoup
import re
import requests
# 请求页面获取html
r=requests.get('http://www.baidu.com').content.decode('UTF-8')
soup=BeautifulSoup(r,'html.parser')# 还有一种格式lxml
# print(type(soup))#解析html文档对象
html=soup.prettify()#美化格式
# print(html)
# print(soup.html.body)#通过标签获取
# print(soup.div)#默认获取第一 

# print(soup.div.form.input.name)#返回标签名
# print(soup.div.form.input.attrs)#返回属性
# print(soup.div.form.input.attrs['name'])#获取属性的值

# print(soup.a.string)
# next_sibling 下一个兄弟节点
# print(soup.div.form.span.next_sibling)
# previous_sibling 上一个兄弟节点
# print(soup.div.form.span.next_sibling.previous_sibling)



'''
查找文档树   fing_all
'''
# 查找所以的span
# print(soup.find_all('span')) 

# 正则匹配
# print(soup.find_all(href=re.compile('http:.*'))) 

# 列表
# print(soup.find_all(['a','span'])) 

# id 
# print(soup.find_all(id='wrapper'))

# class  attrs
# print(soup.find_all(class_='mnav',attrs={'name':'tj_trnews'}))

# text
# print(soup.find_all(text='地图'))

# limit  限定查找个数
print(soup.find_all('a',limit=3))