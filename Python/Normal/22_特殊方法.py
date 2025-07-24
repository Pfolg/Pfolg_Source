# 本程序旨在用最复杂的代码完成最简单的运算
a = 10
b = 20
# print(dir(a))
print(a + b)  # 30
print(a.__add__(b))  # 30 加法
print(a.__sub__(b))  # -10 减法
print(f'{a}<{b}?', a.__lt__(b))
print(f'{a}<={b}?', a.__le__(b))
print(f'{a}=={b}?', a.__eq__(b))
print('-' * 50)
print(f'{a}>{b}?', a.__gt__(b))
print(f'{a}>={b}?', a.__ge__(b))
print(f'{a}!={b}?', a.__ne__(b))
print('-' * 50)
print('乘法', a.__mul__(b))  # *
print('除法', a.__truediv__(b))  # /
print('取余', a.__mod__(b))  # 求余数
print('整除', a.__floordiv__(b))  # 整除
print('幂运算', a.__pow__(2))  # ** or ^
