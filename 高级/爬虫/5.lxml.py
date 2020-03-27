#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree
import requests
r = requests.get(
    'https://www.runoob.com/python/python-100-examples.html').content.decode('utf-8')

html = etree.HTML(r)
# print(type(html))

# 将html文档字符串序列化
result = etree.tostring(html, pretty_print=True,
                        encoding='utf-8').decode('utf-8')
# print(result)

# 选取节点  从根节点匹配
dom = html.xpath('/html/head/meta')  # 已列表形式返回
print(dom)

# 选取节点  匹配标签
dom = html.xpath('//ul')  # 已列表形式返回
print(dom)

'''
.  现在当前节点
.. 选择当前节点的父节点
@  现在属性
'''
