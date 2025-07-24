##
from 平时练习14_内置函数 import list1
import random

print(list1)
space = list1.remove('')
print(space)
print(max(list1))


##
def funct(x):
    a = x[0]
    for i in x:
        if i > a:
            a = i
    print(a)


list2 = [random.randint(1, 100) for j in range(10)]
print(list2)
funct(list2)
print(max(list2))
##
list3 = []
w = input('请输入一个字符串：')
for i in range(len(w)):
    if w[i].isdigit():
        j = eval(w[i])
        list3.append(j)
        s = sum(list3)
    else:
        pass
print(list3, '\n', s)


##
# 字符大小写转换
def lower_upper(x):
    list4 = []
    for i in x:
        if 'A' <= i <= 'Z':
            list4.append(chr(ord(i) + 32))  # ord转为编码，chr转为字符串
        elif 'a' <= i <= 'z':
            list4.append(chr(ord(i) - 32))
        else:
            list4.append(i)
    return ''.join(list4)


jj = input('请输入字符串：')
jk = lower_upper(jj)
print(jk)


##
# def judge(x):
#     list5 = ['Python', 'Java', 'hello', 'world', 'mother', 'earth', 'friend', 'apple', 'cat', 'school']
#     print(len(list5))
#     print(x[len(x)-1])
#     for i in list5:
#         if x == i:
#             print(f'{x}存在于list5')
#         elif i == x[len(x)-1]:
#             print(f'{x}不存在于list5')
#             pass
#         else:
#             pass
#     return x
#
#
# x = input('请输入一个字符串：')
# judge(x)
##
# 一个实现in功能的函数
def judge(it, they):
    for i in they:
        if it == i:
            return True
    return False


they = ['Python', 'Java', 'hello', 'world', 'mother', 'earth', 'friend', 'apple', 'cat', 'school']
it = input('请输入字符串：')
if judge(it, they):
    print("存在")
else:
    print('不存在')
##
