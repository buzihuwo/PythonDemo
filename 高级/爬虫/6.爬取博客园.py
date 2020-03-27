#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}


def download(name, url):
    url = requests.get(url, headers=headers).content.decode('utf-8')
    dsoup = BeautifulSoup(url, 'lxml')
    myContent = dsoup.select('#cnblogs_post_body')
    f1 = open('C:\\Users\\Dell\\Desktop\\pyhton100\\博客园\\%s.txt' %
              name, 'a', encoding='utf-8')
    f1.write(str(myContent))
    f1.close()


r = requests.get('https://www.cnblogs.com/#p1',
                 headers=headers).content.decode('utf-8')
soup = BeautifulSoup(r, 'lxml')
lista = [download(i.text.replace('*', ''), i.attrs['href'])
         for i in soup.select('.post_item a[class="titlelnk"]')]
print('拉取完成')
