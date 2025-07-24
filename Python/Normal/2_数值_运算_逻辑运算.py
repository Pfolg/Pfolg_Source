# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:41:17 2024
嗨喽哇！
@author: Pfolg
"""
print(True+10)# 11
print(False+10)# 10
print(bool(0),bool(0.0))
print(bool(10))# 非0整数的布尔值为True
print(bool(''))
print(bool('你好'))# 非空字符串的布尔值为True
print(bool(False),bool(None))# False 和 None的布尔值是False
print('-------------------------------------')
print(int(3.14))
print(int(3.9))
print(int(-3.14))
print(int(-3.9))# 只保留整数部分，真不戳！
print('------------------')
print(str(8))
print(float('100')+float('200'))
print(ord('程'))# '程'在code表中对应的整数
print(chr(31243))# 与以上相反
print(oct(31243))#转8进制
print(hex(31243))# 转16进制
print(bin(31243))# 转2进制
print('-------------------')
x='欢迎来到成都信息工程大学'
print(eval('x'))# eval 去字符串两端的引号并执行，通常和input连用
x=5
y=6
y+=x
y-=x
y*=x
y/=x
y//=x
y%=x
y**=x
a,b=1,6# 系列解包赋值
a,b=b,a
print(a,b)
# 逻辑运算
print(1>2 or 4>3)
print(not 1>2)
print(1>2 and 5>4)
print('-'*20)
print(not 0)
print(2<<2)#左移位10->1000 (0b)
张=2
李=80
print(李*张)
round(10/3,5)
choice=str(input('你认为原神角色阿蕾奇诺可玩性高吗？(高/中/低):'))
if choice=='高':
    print('那还等什么，赶快收手，屯原石准备抽爆她！！！')
else:
    print('I am really sorry that I cannot give you my suggestions.')
score=int(input('='))
s='666!' if score>80 else '垃圾！'
print(s)
print('666!' if score>80 else '垃圾！')# 越来越NB了
# 多分支
score=float(input('请输入您的成绩='))
if score<0 or score>100:
    print('error!')
elif 0<=score<60:
    print('E')
elif 60<=score<70:
    print('D')
elif 70<=score<80:
    print('C')
elif 80<=score<90:
    print('B')
else:
    print('A')
# 嵌套
output=str(input('win or lose='))
if output=='win':
    print('sleep')
else :
    want=str(input('Do you want end it? yes or no='))
    if want=='yes':
        print('sleep now')
    else:
        print('one more!')
# and 连接多个条件
user=str(input('请输入用户名：'))
pwd=str(input('请输入密码:'))
if user=='csy' and pwd=='qwe123456':
    print('登陆成功！')
elif user!='csy' and pwd=='qwe123456':
    print('用户名错误！')
elif user=='csy' and pwd!='qwe123456':
    print('密码错误！')
else:
    print('登录失败！')
# or
pwd=str(input('请输入您的密码：'))
pin=str(input('请输入您的pin码：'))
fgprt=str(input('指纹是否匹配？ yes/no:'))
if pwd=='666' or pin=='777' or fgprt=='yes':
    print('登陆成功！')
else:
    print('登录失败！')
# random随机数生成
import random
num=random.randrange(0,11)
print(num)
# for
s=0
for i in range(1,101):
    s+=i
print(s)
# while+else
i=int(input('i='))
s=0
k=int(input('k='))
while i<=k:
    s+=i
    print(i)
    i+=1
    if i==999:break#到999停止
else:
    print(s)
# 注册
print('欢迎使用***，请先注册！')
user0=str(input('请输入用户名：'))
pwd0=str(input('请输入密码：'))
# 模拟用户登录
i=0
while i<5:
    user=str(input('请输入用户名：'))
    pwd=str(input('请输入密码：'))
    i+=1
    if user==user0 and pwd==pwd0:
        i=9
        print('登录成功，请稍后，正在进入系统……')
    elif i==5:
        print('对不起，您的次数已用尽，请20分钟后再尝试登陆！')
    else:
        print('用户名或密码有误，您还有',(5-i),'次机会！')

