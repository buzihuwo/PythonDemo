#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(n):
    print('进入第%d层梦境'%n)
    if n==3:
        print('到达潜意识去，意识开始复苏，开始醒来')
    else:
        main(n+1)
    print('从第%d层梦境醒来'%n)

main(1)
        


# 练习  阶层

def jieceng(n):
    if n==1:
        return 1
    else:
        return n*jieceng(n-1)

# 第一步   5*4*3*2       

print(jieceng(5))
