#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
加锁
'''

import threading
balance=0

def chang(n):
    global balance
    balance+=n
    balance-=n


lock=threading.Lock()#获取一个线程锁
def run_thread(n):
    for i in range(100000):
        #获取锁
        lock.acquire()
        try:
            chang(n)
        finally:
            # 释放锁
            lock.release()
        


t1=threading.Thread(target=run_thread,args=(4,))
t2=threading.Thread(target=run_thread,args=(8,))



t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
print(balance)