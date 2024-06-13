# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:59:21 2024
冒泡排序
@author: Pfolg
"""
list1 = []  #name
list2 = []  #score
n = int(input('请输入学生人数：'))
for i in range(0, n):
    item1 = str(input('请输入学生姓名；'))
    item2 = float(input('请输入学生成绩：'))
    list1.append(item1)  #将item1加入list1
    list2.append(item2)  #将item2加入list2
print(list1)
print(list2)

# 以上为高级互动版，若要使用，请注释掉后两行
list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  #name
list2 = [69, 89, 66, 98, 72, 35, 84, 93]  #score
n = len(list1)  #计算list2的元素数
for k in range(0, n):
    for j in range(0, n - k - 1):
        if list2[j] > list2[j + 1]:
            list2[j], list2[j + 1], list1[j], list1[j + 1] = \
                list2[j + 1], list2[j], list1[j + 1], list1[j]  #'\'换行符，第一个for到此处为主要过程
        else:
            pass  #不知道啥用，就是想写，应该没用 还是别写continue了
print('学生人数为：', n)
print(list1)
print(list2)
