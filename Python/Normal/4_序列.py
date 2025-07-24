# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:07:50 2024

@author: Pfolg
"""
# 序列
list1 = 'authorPfolg'
a = len(list1)
print(a)
print(list1[-4])
print(list1[0])
print(list1[0:8:1])
print(list1[:8:2])
print(list1[::-1])
# in and not in
# list1='authorPfolg'
print('a' in list1)  # True
print('b' in list1)  # False
print('a' not in list1)  # False
print('b' not in list1)  # True
#list
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = list('authorPfolg')
print(max(list2))
print(min(list2))
print(list2.index(9))  # 表示查询9第一次出现的索引
print(list1.count('o'))  # 统计list1中o出现的次数（或者说个数）
print(list1 * 3)
print(list1 + list2)
'''
del list1 # 删了
print(list1) # NameError: name 'list1' is not defined
'''
# 遍历
for item in list1:
    print(item)

for i in range(0, len(list1)):
    print(i, list1[i])

for index, item in enumerate(list1):  # 一个用于遍历的函数
    print(index, item)
# List
list3 = list2.copy()
print('list4=', list3)
list2.append(10)  # 在后面加上元素
print(list2)
list2.insert((3), 3.14)  # 在3号位插入元素3.14
print(list2)
a = list2.pop(3)  # 取出3号位元素并从列表中删除
print(a, list2)
list2.remove(10)  # 去除元素10
print(list2)
list2.reverse()  # 使列表反向
print(list2)
list4 = list2.copy()  # 抄袭
print(list4)
list4[8] = '996'
print(list4)
# 列表的排序
print('-' * 90)
print(list2)
list2.sort(reverse=False)  # 排序，默认升序，降序请输reverse=True
print(list2)

import random

list5 = [random.randint(1, 100) for i in range(10)]
print(list5)
list5 = [i for i in range(10) if i % 2 == 0]
print(list5)
