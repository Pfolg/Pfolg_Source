list1 = [546, 5565, 44, 555, 4, 88, 55]
list1.sort()
print('1', list1)
list1.sort(reverse=True)
print('2', list1)
list1.reverse()
print(3, list1)
list1.reverse()
print(4, list1)
list1.remove(555)
print(5, list1)
list2 = ['a', 'b', 'd', 'g', 'h', 'l']
dic1 = zip(list1, list2)
# print(f'dic1\'s type is {type(dic1)}', list(dic1))
a = enumerate(list1, start=1)
print(type(a), tuple(a))
list1.append('')
print(all(list1))  # 判断是否全为bool=1 全为则True
print(len(list1))
print(any(list1))  # 判断是否有bool=1 有则True
list3 = []
print(any(list3))  # False
print('-' * 50)
print(all(list3))  # True 奇怪！
print(next(dic1))
print(next(dic1))
print(next(dic1))
print(next(dic1))
print('-' * 50)


def ji(i):
    return i % 2 == 1


kkk = filter(ji, range(10))
print(list(kkk))
print('-' * 50)


def up(x):
    return x.upper()


list4 = ['hello', 'world', 'java']
mp = map(up, list4)
print(tuple(mp))
############################  其他函数
print(format(3.14, '20'))  # 数值默认右对齐 |                3.14
print(format(3.14, '.3f'))
print(format('hello', '20'))  # str默认左对齐 hello               |
print(format('hello', '*<20'))  # hello***************
print(format('hello', '*>20'))  # ***************hello
##
list5 = ['其他玩家', 'shabi', 'Pfolg', '高端人机玩家']
print('{0} is {1},but {2} is {3}'.format(*list5))  # 解包
##
