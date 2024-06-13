##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取并格式化数据
book1 = pd.read_excel('.\\satellite_x_y_rainfall.xlsx', index_col=None, header=None)
book2 = pd.read_excel('targetPoint_x_y.xlsx', index_col=None, header=None)
work1 = book1.to_numpy()
work2 = book2.to_numpy()

s1_x = work1[:, 0]
s1_y = work1[:, 1]
p_x = work2[:, 0]
p_y = work2[:, 1]

for i in range(len(work2)):
    for j in range(len(work1)):
        if work2[i][0]>=work1[j][0] and work2[i][1]<=work1[j][1]:
            print(work1[j])
## 画图
color = '#0023F5'
# 画线
line_x = np.arange(0, 10, 2)
line_y = np.arange(0, 10, 2)

for i in range(5):
    y = np.zeros(5)
    y[:] += 2 * i
    plt.plot(line_x, y, c=color)

for j in range(5):
    x = np.zeros(5)
    x[:] += 2 * j
    plt.plot(x, line_y, c=color)
# 画点
plt.scatter(s1_x, s1_y, s=60, c=color)
plt.scatter(p_x, p_y, s=60, marker='*', c='#EB3324')
# 画花里胡哨
plt.title('This is a title')
plt.xlabel('Location_x', fontsize=20)
plt.ylabel('Location_y', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
# 画画
plt.show()
##
