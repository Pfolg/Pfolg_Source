# -*- coding: utf-8 -*-
#输入输出
name = input('Please enter your name：')
print('Hello,', name)
age = float(input('PLease input your age:'))
if age >= 18:
    print('Hi,adult!')
else:
    print('Hi,teenager!')
#16进制
a = 0x_a  #0x前缀代表这是个16进制的数
print(a)
#浮点数
print(5e2)  #输出结果为500.0，e代表科学计数法的10
#\ 表示不转义
print('Jack:\'Are you ok?\' Tom:\'Fine,thanks for your caring.\'')

a = float(input('a='))
b = float(input('b='))
a > b
if True:
    print('yes')
else:
    print('no')
#除法
print(10 / 3)  #3.3333333333333335 精确除
print(10 // 3)  #3 取整
print(10 % 3)  #1 取余数
# 参考
s1 = 72
s2 = 85
r1 = (s2 - s1) / s1 * 100
print('小明的成绩提升了 %.1f %%' % r1)
print('小明的成绩提升了{:.1f}%'.format(r1))
print(f'小明的成绩提升了{r1:.1f}%')

#我只能说非常的NICE
x = float(input('x='))
y = float(input('y='))
z = (y - x) / x * 100
print('相比x,y增长了 %s%%' % z)
print('相比{0},y增长了{1:.1f}%'.format('x', z))
print(f'相比{x},{y}增长了{z:.2f}%')
# =============================================================================
# #2024.4.1
# =============================================================================
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[1][0])  #list 输出Java
#条件判断
Weight = float(input('Please input your Weight='))
Height = float(input('Please input your Height='))
BIM = Weight / Height ** 2
if BIM < 18.5:
    print('过轻')
elif BIM >= 18.5 and BIM < 25:
    print('正常')
elif BIM >= 25 and BIM < 28:
    print('过重')
elif BIM >= 28 and BIM < 32:
    print('肥胖')
else:
    print('严重肥胖')
# 匹配模式
Weight = float(input('Please input your Weight='))
Height = float(input('Please input your Height='))
BIM = Weight / Height ** 2
match BIM:
    case x if x < 18.5:
        print('过轻')
    case x if x >= 18.5 and x < 25:
        print('正常')
    case x if x >= 25 and x < 28:
        print('过重')
    case x if x >= 28 and x < 32:
        print('肥胖')
    case x if x >= 32:
        print('严重肥胖')

# =============================================================================
# match——case可匹配：变量、单个值、多个值（用"|"隔开）
# 不行了，遭不住了，今天就到这里吧。呜呜呜……
# =============================================================================
# 2024.4.2

import keyword

print(
    keyword.kwlist)  #['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
import keyword

print(len(keyword.kwlist))

a = b = 1023
print(id(a))  #id=1544626543504
print(id(b))  #id=1544626543504

#0b二 0o八 0x十六

x = 222 + 333j
print('实数部分', x.real)  #222.0
print('虚数\n部分', x.imag)  #333.0 遇\n换行'''
# \的用法

print('北京\n北京\n不急不急不急\t欢迎你')  #\t制表符
print('老师说：\"好好学习，天天向上。\"')  #转义\' \"
print(r'北京\n北京\n不急不急不急\t欢迎你')  # 使转义字符失效：R r'''
# 索引

s = '123456789'
print(s[0], s[-9])
print(s[2:7])  #含2不含7
print(s[-7:-2])  #逆向
print(s[:7])  #默认从0开始

x = '肖丽'
y = '4月3号在寝室打游戏，'
z = '她玩得非常开心，以至于忘了写高数作业'
print(x + y + z)  #'+'表示连接两个字符串

w = 'I love math!'
n = int(input('please enter n='))
print(w * n)  #复制n次，还可以反着写
print('love' in w)  # True
print('hate' in w)  # False
