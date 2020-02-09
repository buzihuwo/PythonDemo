#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import multiprocessing

# 单进程
def work_1(f,n,lock):
    print('work_1 start')
    lock.acquire()#获取锁
    for i in range(n):
        with open(f,'a') as fs:
            fs.write('i love pyhyton \n')
            time.sleep(1)
    lock.release()#释放锁
    print('work_1 end')


def work_2(f,n,lock):
    print('work_2 start')
    lock.acquire()#获取锁
    for i in range(n):
        with open(f,'a') as fs:
            fs.write('come on baby  \n')
            time.sleep(1)
    lock.release()#释放锁
    print('work_2 end')

if __name__=='__main__':
    # 单进程
    # work_1('基础\\xiancheng.txt',3)
    # work_2('基础\\xiancheng.txt',3)
    # 多进程
    lock=multiprocessing.Lock()
    p1=multiprocessing.Process(target=work_1,args=('基础\\xiancheng.txt',3,lock))
    p2=multiprocessing.Process(target=work_2,args=('基础\\xiancheng.txt',3,lock))
    p1.start()
    p2.start()
    


