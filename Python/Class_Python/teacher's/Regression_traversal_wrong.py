# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:28:19 2024

@author: YANG_N
"""


# 定义损失函数（也叫目标函数）
def loss_fun(y1, y2):  # 形参为array变量
    sum = 0
    for i in range(len(y1)):
        temp = (y1[i] - y2[i]) ** 2
        sum = sum + temp
    return sum


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 从excel中读取数据（表格无索引）
df = pd.read_excel(".\\nose.xlsx", index_col=None, header=None)
array = df.to_numpy()
x = array[:, 0]  # x值
y = array[:, 1]  # y值（真值）

# 线性回归-遍历方式，y=wx+b
w = 0.5  # w的初始值
b = 0  # b的初始值
dw = 0.01  # w更新的步长
db = 0.01  # b更新的步长
w_hat = w  # w_hat的初始值
b_hat = b  # b_hat的初始值
loss_value = 9999  # 损失函数的初始值（设置为无穷大）
i_loop = 0  # 初始化循环次数
while w < 5:
    b = 0
    while b < 5:
        y_estimated = w * x + b  # y的估计值
        temp_loss_value = loss_fun(y, y_estimated)  # 计算损失函数值
        if temp_loss_value < loss_value:
            # 满足条件更新（如果损失函数值变小）
            loss_value = temp_loss_value
            w_hat = w
            b_hat = b
        i_loop = i_loop + 1
        b = b + db  # 更新b值
    w = w + dw  # 更新w值
y_hat = w_hat * x + b_hat  # 计算最优函数值y_hat
print(loss_value)
print(f"The estimated function is: ({w_hat}*x + {b_hat})")
print(f"The number of loops is: {i_loop}")
# 画图
dx = 0.5
x_start = 0
x_end = 30
x = np.arange(x_start, x_end + dx, dx)  # # 产生理论数据 - 数值模拟
y_true = 2 * x + 1  # 真实函数关系 (模拟时假设未知)
plt.scatter(x, y, color='b', label='Observed data')
plt.plot(x, y_true, color='r', linewidth=4.0, label='Actual function')
plt.plot(x, y_hat, color='g', linewidth=4.0, label='Estimated function')
plt.xlabel('x', fontsize=20)
plt.ylabel('y', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.legend()
plt.show()

# def loss_fun(y1,y2):
#     sum = 0
#     for i in range(len(y1)):
#         temp = (y1[i] - y2[i]) ** 2
#         sum = sum + temp
#     return sum

# # df = pd.read_excel(".\\linear_regression.xlsx", index_col=None, header=None)
# df = pd.read_excel(".\\linear_regression.xlsx", header=None)
# array = df.to_numpy()
# x = array[:,0].tolist()
# y = array[:,1].tolist()

# w_initial = 0.5
# b_initial = 0
# dw = 0.01
# db = 0.01
# w_hat = w_initial
# b_hat = b_initial
# loss_value = 99999
# while w < 5 and b < 5:
#     y_hat = [i * w_hat + b_hat for i in x]

