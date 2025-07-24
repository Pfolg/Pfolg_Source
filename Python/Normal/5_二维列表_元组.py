# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:53:46 2024

@author: Pfolg
"""
import keyword

print(keyword.kwlist)  # ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# 二维列表
list1 = [
    ['姓名', '身高', '体重'],
    ['小明', '180', '55'],
    ['王华', '173', '53'],
    ['小红', '168', '50']
]
for i in list1:
    for j in i:
        print(j, end='\t')
    print()
# 列表生成式
list2 = [[j for j in range(5)] for i in range(4)]
print(list2)
for i in list2:
    for j in i:
        print(j, end='\t')
    print()
# 元组
tuple1 = (8, 0, 4, 99, 23, 2024)  # i for i in random.randint(1, 100) for j in range(10)
print(tuple1)
print(0 in tuple1)
print(10 in tuple1)
print(tuple1.count(2024))
print(tuple1.index(2024))
print(len(tuple1))
print(max(tuple1))
print(min(tuple1))
# 元组的删除
y = (1,)
print(y, type(y))
'''
del y
print(y) # name 'y' is not defined
'''
# 元组的访问与遍历
print(tuple1[0])
for i in range(len(tuple1)):
    print(tuple1[i], end='\t')

for index, item in enumerate(tuple1, start=4):  # 序号（index）从4开始输出
    print(index, item)
# 元组生成式
# import random
t1 = (j for j in range(10))
print(t1)
# t2=tuple(t1)
# print(t2)
print(t1.__next__())
print(t1.__next__())
print(t1.__next__())
t2 = tuple(t1)
print(t2)  # 可以看到0.1.2都不在元组t1内了
# 字典 Dictionary 使用列表创建字典
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd', 'e']
dic1 = zip(list1, list2)
print(dic1)  # <zip object at 0x000001C5764834C0>
# print(list(dic1)) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
print(dict(dic1))  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# 使用参数创建字典
a = dict(c=1, b=2)
print(a)
# 元组可以作为字典的键
t = (3, 8, 9)
print({t: 10})  # {(3, 8, 9): 10} 但是列表不可以作为字典的键
# del a # 字典的删除
# print(a) # 删除后报错 name 'a' is not defined
'''Dictionary访问与遍历'''
d = {'a': 10, 'c': 3, 'r': 99, 'f': 4}
print(d)
print(d['f'])  # 无f报错
print(d.get('f'))  # 二者是有区别的，可指定默认值
# print(d['x']) KeyError: 'x'
print(d.get('x'))  # None
print(d.get('x', '无'))  # 没有x指定输出无
for i in d.items():
    print(i, end='')
print()
for j in d.keys():
    print(j, end='')
print()
for k in d.values():
    print(k, end='')
print('-' * 50)
d['y'] = 6
print(d)  # 向字典中添加元素
d.pop('y')
print(d)  # 取出并删除'y'及其对应的value
x = d.popitem()
print(x)
print(d)
d.clear()  # 清空字典中元素
print(d)

print('-' * 50)
# 字典生成式
import random

Dictionary1 = {item: random.randint(1, 100) for item in range(0, 11)}
print(Dictionary1)
print('-' * 50)
list1 = [1, 2, 3, 4]
list2 = [2, 4, 6, 8]
Dictionary2 = {a: k for a, k in zip(list1, list2)}
print(Dictionary2)

# 集合，只能存储不可变数据类型，无序,不能存列表
print('-' * 50)
s1 = {1, 2, 3, 4}
print(s1)
s2 = set([1, 2, 3, 4])
print(s2)
s3 = set('helloworld')
print(s3)
s4 = set(random.randint(1, 100) for i in range(10))
print(s4)
print(len(s4))
print(max(s4))
print(min(s4))
# 集合运算
print('-' * 50)
s5 = s1 & s4  # 交
print('s1 & s4', s5)
s6 = s1 | s4  # 并
print('s1 | s4', s6)
s7 = s1 - s4  # 差
print('s1 - s4', s7)
s8 = s1 ^ s4  # 补
print('s1 ^ s4', s8)
# 集合操作
print('-' * 50)
s8.add(888)
print(s8)
s8.remove(888)
print(s8)
'''
s8.remove(888)
print(s8) # KeyError: 888'''
# s8.clear()
# print(s8)
for i, j in enumerate(s8):
    print(i, j)
# 字典合并
print('-' * 50)
Dictionary3 = Dictionary1 | Dictionary2
print(Dictionary3)
list10 = [1, 2, 3, 4, 5]
print(list10.reverse())
