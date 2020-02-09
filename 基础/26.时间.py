#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
# 当前时间的时间搓
print(time.time())
#当前时间
print(time.ctime())
print(time.ctime(time.time()))

# 返回当前时间的时间元祖
print(time.localtime())

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# 练习
'''
将字符串时间转成时间搓
'''
# 将字符串时间转换成元祖
print('%s%s%s'%('-'*10,'练习','-'*10))
print('%s%s%s'%('-'*10,'将字符串时间转换成元祖','-'*10))
times='2020-2-2 11:05:20'
formatTime= time.strptime(times,'%Y-%m-%d %H:%M:%S')
print(formatTime)
# 将时间元祖转换成时间戳
print('%s%s%s'%('-'*10,'将时间元祖转换成时间戳','-'*10))
print(time.mktime(formatTime))

'''
把时间2020-2-2 11:05:20改成2020/2/2 11:05:20
'''
print('%s%s%s'%('-'*10,'把时间2020-2-2 11:05:20改成2020/2/2 11:05:20','-'*10))
times1='2020-2-2 11:05:20'
formatTime1= time.strptime(times1,'%Y-%m-%d %H:%M:%S')#strptime() 函数根据指定的格式把一个时间字符串解析为时间元组
print (time.strftime('%Y/%m/%d %H:%M:%S',formatTime1))

'''
获取当前时间戳转换指定格式日期
'''
print('%s%s%s'%('-'*10,'获取当前时间戳转换指定格式日期','-'*10))
time2=time.time()
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time2))) #strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间

'''
获取前三天的时间
'''
print('%s%s%s'%('-'*10,'获取前三天的时间','-'*10))
import datetime
nowdime=datetime.datetime.now()
print((nowdime+datetime.timedelta(days=-3)).strftime('%Y/%m/%d %H:%M:%S'))




