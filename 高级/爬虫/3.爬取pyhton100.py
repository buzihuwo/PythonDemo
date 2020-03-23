#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


def getContent(url,name):
    r=requests.get(url,headers).content.decode('UTF-8')
    html=BeautifulSoup(r,'lxml')
    myContent=html.find(id='content')
    f1=open('C:\\Users\\Dell\\Desktop\\pyhton100\\%s.txt'%name,'a',encoding='utf-8')
    f1.write(myContent.text)
    f1.close()

headers={
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36' 
}
r=requests.get('https://www.runoob.com/python/python-100-examples.html',headers=headers).content.decode('UTF-8')
soup=BeautifulSoup(r,'lxml')
list100=[{'url':'https://www.runoob.com%s'%i.attrs['href'],'name':i.string} for i in soup.find(id='content').ul.find_all('a')]
for i in list100:
    getContent(i['url'],i['name'])
print('拉起完成')