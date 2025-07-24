import random as rd

n = int(input('请输入测试次数：'))
j = 0
for i in range(n):
    x = rd.uniform(-2, 2)  # x
    y = rd.uniform(-2, 2)  # y
    if x ** 2 + y ** 2 <= 4:
        j += 1
p = (j / n)
q = p * 4
print(p, q)

import math
import random

list_x = list()
list_y = list()
n = int(input('请输入测试次数：'))
A = 0
for i in range(n):
    x, y = random.uniform(-2, 6), random.uniform(-6, 2)
    list_x.append(x)
    list_y.append(y)
for j in range(n):
    a, b = list_x[j], list_y[j]
    if math.sqrt((a - 2) ** 2 + (b + 2) ** 2) < 4:
        A += 1
P = A / n
print('{0:.4f},{1:.4f}'.format(P, P * 4))

# 画图
import matplotlib.pyplot as plt
import numpy as np

# 画圆
theta = np.linspace(0, 2 * np.pi, 100)
x = 2 + 4 * np.cos(theta)
y = -2 + 4 * np.sin(theta)
plt.plot(x, y, color='black', linewidth=4.0)
plt.scatter(2, -2, s=100, linewidth=2.0, edgecolors='g', facecolors='none')
# 画半径的箭头
circle_point_1 = 2 + math.sin(math.pi / 4)
circle_point_2 = 2 + math.cos(math.pi / 4)
plt.arrow(2, -2, circle_point_1, circle_point_2, head_width=0.15, head_length=0.15, width=0.05, color='c')
# 画正方形
x_square = [-2, 6, 6, -2, -2]
y_square = [2, 2, -6, -6, 2]
plt.plot(x_square, y_square, color='black', linewidth=4.0)
# 坐标轴字体大小
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
# 设置坐标轴名称
plt.xlabel('x', fontsize=20)
plt.ylabel('y', fontsize=20)
plt.show()
