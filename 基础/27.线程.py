#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

def music(name,loop):
    for i in range(loop):
        print('listen music %s %s %s'%(name,time.ctime(),threading.Thread.getName(t1)))
        time.sleep(1)

def mocie(name,loop):
    for i in range(loop):
        print('look mocie %s %s %s'%(name,time.ctime(),threading.Thread.getName(t2)))
        time.sleep(1)

t1=threading.Thread(target=music,args=('爱的故事',4),name='线程一')
t2=threading.Thread(target=mocie,args=('肖生克的救赎',3),name='线程二')

if __name__=='__main__':
    # 守护主线程，主线程结束杀死子线程，必须早线程开始的时候添加,子线程不能等待
    # t1.setDaemon(True)
    # t2.setDaemon(True)
    
    # 启动线程
    t1.start()
    t2.start()

    # join可以对主线程进行阻塞，等所有的子线程运行结束在进行主线程
    # t1.join()
    # t2.join()
    
    # 线程的标识符
    print('t1线程的标识符 %s'%t1.ident)
    print('t2线程的标识符 %s'%t2.ident)


        