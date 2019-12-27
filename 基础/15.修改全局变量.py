#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a=1
def text1():
    global a # 声明修改全局变量
    a=2
    print(a)

print(a)
text1()
print(a)


# ----------------------------------练习

# 登录
def login(pwd):
    myPwd='88888'
    # if isinstance(pwd,int)==False:
    #     return '类型必须是int型'
    return True if pwd==myPwd else False
# 金额验证
def checkMoney(money):
    if money.isdigit():
        myoney=int(money)
        if myoney %100==0 and 0<=100<=1000:
            return True
        else:
            return False
    else:
        return False
        
            
        
def main():
    for i in range(0,3):
        if login(input('清输入密码：')):
            while True:
                money=input('请输入金额：')
                if checkMoney(money):
                    print('您成功取出%s'%money)
                    break
                else:
                    print('您输入的金额有误，请重新输入。')
            print('交易完成')
        else:
            print('密码不对')





main()


