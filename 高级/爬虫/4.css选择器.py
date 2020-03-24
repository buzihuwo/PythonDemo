#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
r = requests.get('https://www.runoob.com/python/python-100-examples.html',
                 headers=headers).content.decode('UTF-8')
soup = BeautifulSoup(r, 'lxml')
#  查找id
print('%s%s%s' % ('-'*20, '查找id', '-'*20))
print(soup.select('#content'))

#  查找标签
print('%s%s%s' % ('-'*20, '查找标签', '-'*20))
print(soup.select('#content h1'))

#  查找类名
print('%s%s%s' % ('-'*20, '查找类名', '-'*20))
print(soup.select('.previous-design-link'))

#  通过属性查找
print('%s%s%s' % ('-'*20, '通过属性查找', '-'*20))
print(soup.select('a[title="Python 练习实例1"]'))

#  组合查找
print('%s%s%s' % ('-'*20, '组合查找', '-'*20))
print(soup.select('.article-body #content'))

#  获取内容
print('%s%s%s' % ('-'*20, '获取内容', '-'*20))
print(soup.select('#content a')[0].get_text())  # 或者是text
