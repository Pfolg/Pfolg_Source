# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:59:09 2024

@author: Pfolg
"""

str1='hello,'
str2='world!'
print(str1+str2)

for i in range(1,10):
    print(i)

a = 6
print(id(a))

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # break continue=跳过3，break=3处停止
    print(i)
a = 'python '
print(a * 10)
print(id(' '))
b = 'apple'
print(len(b))
print(max(b))
print(min(b))
print(b[-5])
print(dir(str))
inventors = 'edison,tesla,newton'
inventors_split = inventors.split(',')
print(inventors_split)
print(inventors[15])
print(inventors_split[2])
# 索引
phrase = "hello world!"
print(phrase[0])
print(phrase[4:10])
print(phrase[4:10:2])
print(phrase[4:10:3])
print(phrase[4:])
print(phrase[-1])
# complaint
print('----------------')
complaint = 'The second class is a piece of shit!'
print(complaint + 'he，tui！！！')
print('----------------')
alphabet = 'google'
index = 0
print(f"In the string '{alphabet}'")
for each_char in alphabet:
    print(f"Character'{each_char}'-index is {index}")
    index += 1
# 感受list的魅力
list_1 = [1, 3, 5, 7]
list_2 = [2, 4, 6, 8]
print(list_1 + list_2)
print(list_1 * 3)
print(list_1 == list_2)
print(5 in list_1)
print(5 not in list_2)
# list可以修改值
list_1 = [1, 3, 5, 7, "apple", "orange"]
list_1[0] = "apple"
print(list_1)
print(list_1[0:2])
# 用list，range，sum函数求1-100的和
a = list(range(1, 101, 1))
print(type(a))
print('The sum from 1 to 100 is ' + str(sum(a)))
# pop
b_list = ['Albert', 'Johnson', 'james', 'Emily']
print(b_list)
b_pop = b_list.pop(0)
print(b_pop)
print(b_list)
# list.append
list_of_items = []
no_of_items = 3
for i in range(no_of_items):
    item = input(f'enter item{i}:')
    list_of_items.append(item)
    print(list_of_items)
