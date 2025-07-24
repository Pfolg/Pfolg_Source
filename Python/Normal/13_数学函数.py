import math

a = -5
b = 5
i = 0
c = abs(a)
print(c)
d, e = divmod(a, b)
print(d, e)
f = max(a, b, c, d, e)
print(f)
g = min(a, b, c, d, e)
print(g)
list1 = []
for h in range(1, 11):
    list1.append(h)
    i = sum(list1)
print(i)
k = pow(a, b)
print(k)
m = round(math.pi, 7)  # 只有一个参数时只保留整数 四舍五入
print(m)
n = round(math.pi * 100, -1)
print(n)
