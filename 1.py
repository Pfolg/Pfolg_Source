a = 128
b = 1024
c = 512
d = a + \
    b - \
    c
print(d)

a = float(input())
if a > 10:
    print('NULL')
elif a <= 0:
    print('NULL')
else:
    print('The number we need.')  #1 有问题  2 舒服了

a = 0b101
b = bin(5)
c = int('101', 2)
print(a, b, c)

# import 课堂小记_Dictionary
# v1=9
# v2=3
# a=课堂小记_Dictionary.my_add(v1,v2)#实际参数
# print(f"my_add function:{v1}+{v2}={a}")


year = int(input('请输入1800年到2024年中的一个年份：'))
if year < 1800 or year > 2024:
    year = int(input('请重新输入1800年到2024年中的一个年份：'))
for i in range(10):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f'{year}年是闰年！')
    else:
        print(f'{year}一年不是闰年！')
