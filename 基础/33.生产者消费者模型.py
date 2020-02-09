#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time
import queue

q= queue.Queue(maxsize=10)

# 生产者
def producer(name):
    count=1
    while True:
        q.put('骨头%s'%count)
        print('生产了骨头',count)
        count+=1
        time.sleep(0.5)

# 消费者
def consumer(name):
    while True:
        print('[%s]取得[%s]并吃了它..'%(name,q.get()))
        time.sleep(1)

p=threading.Thread(target=producer,args=('Tim',))
c1=threading.Thread(target=consumer,args=('King',))
c2=threading.Thread(target=consumer,args=('Wang',))

p.start()
c1.start()
c2.start()