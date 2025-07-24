# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:21:51 2024
使用嵌套打印图形（个人觉得不太好看）
@author: Pfolg
"""
# 在print()输出语句后面加入end='',以防止print()输出语句自动换行，
# 通过end=''将输出结果放在同一行，输出结果之间的间隔数取决于引号间的空格数。
# 打印 矩形
for i in range(1,4):#行
    for j in range(1,5):#列
        print('*',end='')
    print()#换行
# 三角形1
for i in range(1,6):#行
    for j in range(1,i+1):#列
        print('*',end='')
    print()#换行
# 三角形2
for i in range(1,7):#行
    for j in range(1,7-i):#列
        print('*',end='')
    print()#换行
# 等腰三角形
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print()
# 菱形 自己尝试写的
for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print()
for g in range(1,4):
    for h in range(1,g+1):
        print(' ',end='')
    for f in range(1,(4-g)*2):
        print('*',end='')
    print()
# 菱形 请输入菱形行数
row_top=int(input('请输入菱形行数：'))
while row_top%2==0:
    row_top=int(input("请重新输入行数："))
print('行数=',row_top)
row=int((row_top+1)//2)
for i in range(1,row+1):
    for j in range(1,row+1-i):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print()
for g in range(1,row):
    for h in range(1,g+1):
        print(' ',end='')
    for f in range(1,(row-g)*2):
        print('*',end='')
    print()
# 空心菱形
row_top=int(input('请输入菱形行数：'))
while row_top%2==0: # 确认菱形的行数是奇数
    row_top=int(input("请重新输入行数："))
print('行数=',row_top)
row=(row_top+1)//2
for i in range(1,row+1):# 上半部分
    for j in range(1,row+1-i):
        print(' ',end='') # 前边的空格
    for k in range(1,2*i): # 后面的轮廓
        if k==1 or k==2*i-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for g in range(1,row):# 下半部分
    for h in range(1,g+1):
        print(' ',end='') # 空格
    for f in range(1,(row-g)*2): # 轮廓
        if f==1 or f==(row-g)*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
print('你可能会觉得这很没用，但道理和打游戏赢了一样，无需在意，我自体会其乐趣！')