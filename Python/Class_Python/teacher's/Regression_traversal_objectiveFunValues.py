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
df = pd.read_excel(".\\linear_regression.xlsx", index_col=None, header=None)
array = df.to_numpy()
x = array[:, 0]  # x值
y = array[:, 1]  # y值（真值）

# 线性回归-遍历方式，y=wx+b
w = 0.5  # w的初始值
dw = 0.01  # w更新的步长
db = 0.01  # b更新的步长
w_hat = w  # w_hat的初始值
b_hat = 0  # b_hat的初始值
loss_value = 9999  # 损失函数的初始值（设置为无穷大）
i_loop = 0  # 初始化循环次数
w_vector = np.zeros(int((5 - 0.5) / dw + 1))  # W_vector
b_vector = np.zeros(int((5 - 0) / db + 1))  # b_vector
L_matrix = np.zeros((len(w_vector), len(b_vector)))  # L matrix
m = 0  # index for w_vector
while w < 5:
    w_vector[m] = w
    n = 0  # index for b_vector
    b = 0  # b的初始值
    while b < 5:
        b_vector[n] = b
        y_estimated = w * x + b  # y的估计值
        temp_loss_value = loss_fun(y, y_estimated)  # 计算损失函数值
        L_matrix[m, n] = temp_loss_value  # L matrix
        if temp_loss_value < loss_value:
            # 满足条件更新（如果损失函数值变小）
            loss_value = temp_loss_value
            w_hat = w
            b_hat = b
        i_loop = i_loop + 1  # 循环次数更新
        b = b + db  # 更新b值
        n = n + 1  # index for b_vector
    w = w + dw  # 更新w值
    m = m + 1  # index for w_vector
y_hat = w_hat * x + b_hat  # 计算最优函数值y_hat
print(f"The estimated function is: ({w_hat}*x + {b_hat})")
print(f"The number of loops is: {i_loop}")

# 伪三维图，即目标函数颜色图
fig, ax = plt.subplots()
L_matrix_2 = L_matrix ** 0.1  # 突出颜色
L_matrix_2 = L_matrix_2 - L_matrix_2.min()
L_matrix_2 = L_matrix_2 / L_matrix_2.max()
im = ax.imshow(L_matrix_2, cmap='viridis', \
               extent=[b_vector.min(), b_vector.max(), \
                       w_vector.max(), w_vector.min()])
cbar = ax.figure.colorbar(im, ax=ax)
plt.xlabel('b', fontsize=20)
plt.ylabel('w', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.show()

fig, ax = plt.subplots()
plt.plot(w_vector, L_matrix[:, 200])
plt.xlabel('w', fontsize=20)
plt.ylabel('L', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.show()

# 频率分布直方图 - w
fig, ax = plt.subplots()
plt.hist(w_vector, bins=20, color='b', edgecolor='k', linewidth=1.5)
plt.xlabel('w', fontsize=20)
plt.ylabel('Number', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.show()

# 频率分布直方图 - b
fig, ax = plt.subplots()
plt.hist(b_vector, bins=20, color='b', edgecolor='k', linewidth=1.5)
plt.xlabel('b', fontsize=20)
plt.ylabel('Number', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.show()

# w b 和 L的图放在一张画布上面
fig, ax = plt.subplots(2, 2)
ax[0, 0].hist(w_vector, bins=20, color='b', edgecolor='k', linewidth=1.5)
ax[0, 1].imshow(L_matrix_2, cmap='viridis', \
                extent=[b_vector.min(), b_vector.max(), \
                        w_vector.max(), w_vector.min()])
ax[1, 1].hist(b_vector, bins=20, color='b', edgecolor='k', linewidth=1.5)
ax[1, 0].set_axis_off()
plt.show()
