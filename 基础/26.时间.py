#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
# d当前时间的时间搓
print(time.time())
#当前时间
print(time.ctime())
print(time.ctime(time.time()))

# 返回当前时间的时间元祖
print(time.localtime())

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))