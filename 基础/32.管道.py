#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import multiprocessing

def put(q):
    for value in ['A','B','C','D']:
        print('发送 %s 到 pipe ...'%value)
        q[1].send(value)
        time.sleep(2)

def get(q):
    while True:
        value=q[0].recv()
        print('从 pipe 接受 %s .'%value)

if __name__=='__main__':
    q=multiprocessing.Pipe(duplex=False)#duplex=False是左收右发  duplex=True双通道
    pw=multiprocessing.Process(target=put,args=(q,))
    pr=multiprocessing.Process(target=get,args=(q,))
    pw.start()
    pr.start()

    pw.join()
    #pr进程是死循环，无法等待结束，只能强制终止
    pr.terminate()