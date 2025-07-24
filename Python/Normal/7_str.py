# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:28:21 2024

@author: Pfolg
"""
import math
print(2*math.pi)
str1='Populating the interactive namespace from numpy and matplotlib'
str2=str1.startswith('666')
print(str2) # 判断str1是否以‘*’开头
str3=str1.endswith('6969999')
print(str3) # 判断str1是否以‘*’结尾
print('-'*50)
str4=str1.upper()
print(str4) # 全大写 POPULATING THE INTERACTIVE NAMESPACE FROM NUMPY AND MATPLOTLIB
str5=str1.lower()
print(str5) # 全小写 populating the interactive namespace from numpy and matplotlib
list1=str1.split(sep=' ') # 以 分隔str1，输出结果为list类型
print(list1) # ['Populating', 'the', 'interactive', 'namespace', 'from', 'numpy', 'and', 'matplotlib']
print('-'*50)
print(str1.count('a')) # 统计a出现的次数 6
print(str1.count('x')) # 0
print(str1.find('a')) # 5
print(str1.find('x')) # -1 就是不存在的意思
print(str1.index('a')) # 5 与find差不多，不过找不到会报错
# print(str1.index('x')) # ValueError: substring not found
print('-'*50)
# 替换
str6=str1.replace('a','部落冲突',3) # 替换三次
print(str6)
# 居中
str7='1234567890'.center(20,'-') # 可以不加-
print(str7) # -----1234567890-----
# 去除
print('     hello     world     '.strip()) # hello     world——去两边
print('     hello     world     '.lstrip()) # hello     world     ——去左边
print('     hello     world     '.rstrip()) #      hello     world——去右边
print('python-pythonpy'.strip('py')) # thon-python 居然不能去中间的吗?
print('剩余操作同上')
print('-'*50)
# 巴拉巴拉
name='liu'
age=18
score=98.5
print('name:%s,age:%d,score:%.4f' % (name,age,score)) # name:liu,age:18,score:98.5000
# f string
print(f'name:{name},age:{age},score:{score}') # 效果差不多
# format
print("name:{0},age:{1},score:{2}".format('lu',28,100)) # name:lu,age:28,score:100
# format格式控制
str8='悄悄努力，默默变强'
print('{0:*<20}'.format(str8)) # 左对齐，后面用*填充
print('{0:*>20}'.format(str8)) # 右对齐
print('{0:*^20}'.format(str8)) # 居中
print(str8.center(20,'*')) # 居中，效果与上一行一致
# 千位分隔符，只适用于整数和浮点数
print('{0:,} | {1:,}'.format(66666,987654321.6666)) # 66,666 | 987,654,321.6666
import math
print('{0:.4f}'.format(math.pi))
print('{0:.5}'.format('Populating the interactive namespace from numpy and matplotlib')) # Popul
# 进制表示——整数
print('二进制：{0:b},十进制：{0:d},八进制：{0:o},十六进制：{0:x}'.format(456))
# float
print("{0:.3f},{0:2e},{0:2%}".format(math.pi)) # 3.142,3.141593e+00,314.159265%