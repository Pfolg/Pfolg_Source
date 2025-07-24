##
def ct(a, b, c):
    #  局部变量的优先级更高 cosarf, cosbt, cosgm 是局部变量
    cosarf = a / (a ** 2 + b ** 2 + c ** 2) ** 0.5
    cosbt = b / (a ** 2 + b ** 2 + c ** 2) ** 0.5
    cosgm = c / (a ** 2 + b ** 2 + c ** 2) ** 0.5
    print(cosarf, cosbt, cosgm)  # 这三个是形参
    return cosarf, cosbt, cosgm


ct(3, 4, 5)  # 这里的是实参
ct(13, 14, 15)
##
# 关键字传参
ct(c=7, a=6, b=8)  # 位置参数在前，关键字参数在后


##
def bt(a=3, b=4, c=5):  # 默认值参数
    cosar = a / (a ** 2 + b ** 2 + c ** 2) ** 0.5
    cosbt = b / (a ** 2 + b ** 2 + c ** 2) ** 0.5
    cosgm = c / (a ** 2 + b ** 2 + c ** 2) ** 0.5
    print(cosar, cosbt, cosgm)  # 这三个是形参


bt()


##
#  个数可变的位置参数
def func(*s):
    print(type(s))
    for i in s:
        print(i, end=' ')


func(1, 2, 3)
print()
func(9, 8, 7, 4, 5, 6, 1, 2, 3)
#  调用时，在参数前加一颗星，将对元素进行解包输出
print()
func(['vv', 'ff', 'dami', 'sasa', 'bdjs'])
print()
func(*['vv', 'ff', 'dami', 'sasa', 'bdjs'])


##
#  个数可变的关键字参数
def func1(**x):
    print(type(x))
    for i, j in x.items():
        print(i, '-->', j)  # i key,j value


func1(电脑='3600', 手机='2000', 鼠标='60', 我='0')
d = {'电脑': '3600', '手机': '2000', '鼠标': '60', '我': '0'}
l1 = ['电脑', '手机', '鼠标', '我']
l2 = [3600, 2000, 60, 0]
d1 = dict(zip(l1, l2))
print('d1为', d1)
# func1(d)  # ypeError: func1() takes 0 positional arguments but 1 was given
func1(**d)  # 系列解包操作
func1(**d1)


##


def sumx(a, b):
    global s  # 定义s为全局变量
    s = 0
    for i in range(a, b + 1):
        s += i
    print(s)


sumx(1, 10)
print(s)  # 可以输出s


# print(i)  # NameError: name 'i' is not defined.所以i是局部变量
##
def sumx(a, b):
    global s, i  # 定义s为全局变量
    s = 0  # 声明和赋值要分开
    for i in range(a, b + 1):
        s += i
    print(s)


sumx(1, 10)
print(s)  # 可以输出s
print(i)

##
#  匿名函数lambda
s = lambda a, b: a + b
print(type(s))  # <class 'function'>
print(s(1, 10))
##
list1 = [1, 2, 3]
for i in range(len(list1)):
    re = lambda sy: sy[i]
    print(type(re))
    print(re(list1))
##
list3 = [{'name': 'sam', 'score': 80},
         {'name': 'tom', 'score': 63},
         {'name': 'marry', 'score': 98},
         {'name': 'daming', 'score': 67},
         {'name': 'Pflog', 'score': 100}, ]
list3.sort(key=lambda x: x['score'], reverse=True)
print(list3)
for i in range(len(list3)):
    print(list3[i]['name'], '-->', list3[i]['score'])


##
# 递归  阶乘
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)  # 自己调用自己


n = int(input('n='))
print(fac(n))


##
# 斐波那契数列
def fa(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fa(n - 1) + fa(n - 2)


n = int(input('n='))
print(fa(n))
##
