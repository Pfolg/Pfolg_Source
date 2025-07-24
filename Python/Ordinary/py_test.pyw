import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# 设置中文字体
font_path = 'C:/Windows/Fonts/simhei.ttf'  # SimHei 字体路径（Windows 系统）
font_prop = font_manager.FontProperties(fname=font_path)

# 定义液滴半径范围（微米）
r = np.logspace(-2, 1, 400)  # 从0.01到10微米，共400个点

# 不同成分的Cr和Cn值（单位：kg）
Cr_values = [
    0,              # 纯水
    1e-19,          # 10^-19 kg 氯化钙
    1e-18,          # 10^-18 kg 氯化钙
    1e-17,          # 10^-17 kg 氯化钙
    1e-19,          # 10^-19 kg 硫酸钙
    1e-18           # 10^-18 kg 硫酸钙
]

Cn_values = [
    0,              # 纯水
    0,              # 10^-19 kg 氯化钙
    0,              # 10^-18 kg 氯化钙
    0,              # 10^-17 kg 氯化钙
    1e-19,          # 10^-19 kg 硫酸钙
    1e-18           # 10^-18 kg 硫酸钙
]

# 图例标签
labels = [
    '纯水',
    '10^-19 kg 氯化钙',
    '10^-18 kg 氯化钙',
    '10^-17 kg 氯化钙',
    '10^-19 kg 硫酸钙',
    '10^-18 kg 硫酸钙'
]

plt.figure(figsize=(10, 6))

# 绘制每条曲线
for Cr, Cn, label in zip(Cr_values, Cn_values, labels):
    # Kohler方程：Ern / E∞ = 1 + Cr / r - Cn / r^3
    Ern_Einf = 1 + Cr / r - Cn / r**3
    plt.plot(r, Ern_Einf, label=label)

# 设置坐标轴为对数尺度
plt.xscale('log')

# 设置x轴和y轴的范围
plt.xlim(0.01, 10)  # x轴范围从0.01到10微米
plt.ylim(0.9, 1.1)  # y轴范围从0.9到1.1

# 添加坐标轴标签和标题，使用中文字体
plt.xlabel('液滴半径 r (μm)', fontproperties=font_prop, fontsize=14)
plt.ylabel('相对湿度 (%) / 过饱和度 (%)', fontproperties=font_prop, fontsize=14)
plt.title('寇拉曲线：不同成分溶液滴的相对湿度与半径关系', fontproperties=font_prop, fontsize=16)

# 添加图例
plt.legend(prop=font_prop)

# 显示网格
plt.grid(True, which='both', ls='--', linewidth=0.5)

# 显示图形
plt.show()