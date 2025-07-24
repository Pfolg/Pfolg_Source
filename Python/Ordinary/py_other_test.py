import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import AutoMinorLocator

# 定义 r 的范围
r = np.arange(0.01, 10, 0.001)

# 定义常数
cr = 0.0022
cn = 0.147 * 10e-18 * 10e12

# 定义 y 的计算公式
y = 1 + cr / r - cn / r ** 3

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制曲线
ax.plot(r, y, label='y')

# 设置 x 轴和 y 轴的范围
ax.set_xlim(0.01, 10)  # x 轴范围从0.01到10微米
ax.set_ylim(0.8, 1.05)  # y 轴范围从0.8到1.05

# 设置 x 轴为对数尺度
ax.set_xscale('log')

# 设置 x 轴标签
ax.set_xlabel('液滴半径 (μm)', fontsize=12)

# 设置 y 轴标签
ax.set_ylabel('相对湿度或过饱和度 (%)', fontsize=12)

# 设置 y 轴刻度间隔
# 在 0.8 到 1.0 之间使用 0.05 的间隔
ax.yaxis.set_major_locator(MultipleLocator(0.05))

# 在 1.0 到 1.05 之间使用 0.01 的间隔
# 可以添加一个次刻度定位器
ax.yaxis.set_minor_locator(AutoMinorLocator(5))  # 5个次刻度间隔

# 添加网格
ax.grid(True, which='both', ls='--', linewidth=0.5)

# 添加图例
ax.legend(loc='upper left')

# 显示图形
plt.title('液滴半径与相对湿度或过饱和度关系图', fontsize=14)
plt.show()