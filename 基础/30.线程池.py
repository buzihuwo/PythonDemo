#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import multiprocessing
import time

def work(n):
    print('运行(%s),进程ID%s'%(n,os.getpid()))
    time.sleep(5)
    print('运行(%s)结束,进程ID%s'%(n,os.getpid()))

if __name__=='__main__':
    print('父进程ID%s'%os.getpid())
    #创建进程池
    p=multiprocessing.Pool(3)
    for i in range(5):
        #创建5个进程，一次进入进程池
        p.apply_async(work,args=(i,))
    p.close()
    p.join()