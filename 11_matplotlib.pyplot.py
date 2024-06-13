"""
我写的shi
"""
##
# import numpy as np
# import matplotlib.pyplot as plt
# import math
# import random
#
# miu = 2
# sgm = 3
# x = np.array([random.uniform(-4 * sgm, 4 * sgm) for i in range(100)])
#
#
# print(x)
#
#
# ##
#
# def x_N(m, s, x1):
#     f = (math.e ** (-(x1 - m) ** 2 / s ** 2)) / s * (2 * math.pi) ** 0.5
#     return f
#
#
# fx = x_N(miu, sgm, x)
# print(fx)
# plt.plot(x, fx, c='#000000')
# plt.tick_params(axis='x', labelsize=20)
# plt.tick_params(axis='y', labelsize=20)
# plt.xlabel('x', fontsize=20)
# plt.ylabel('fx', fontsize=20)
# plt.show()
# ##

import matplotlib.pyplot as plt
import numpy as np

mu, sgm = 2, 3

x = np.linspace(-4 * sgm, 4 * sgm, 100)

gaussian = np.exp(-(x - mu) ** 2 / (2 * sgm ** 2)) / (np.sqrt(2 * np.pi) * sgm)
try:
    plt.plot(x, gaussian, c='#000000')
    plt.title(f'Guassian distribution - $\mu={mu},\sigma$={sgm}', fontsize=20)
    plt.xlabel('x', fontsize=20)
    plt.ylabel('f(x)', fontsize=20)
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.show()
except SyntaxWarning:
    pass
##
#模拟小球从10m高空下落的 时间—高度
import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(10, 0, 21)
h0 = 10
g = 9.8
t = np.sqrt(2 * (h0 - y) / g)
# plt.plot(t, y, "-*b")
# plt.xlabel("time(s)", fontsize=20)
# plt.ylabel("position(m)", fontsize=20)
# plt.tick_params(axis="x", labelsize=20)
# plt.tick_params(axis="y", labelsize=20)
# plt.show()

import pandas as pd

t_y = np.vstack((t, y))
t_y = np.transpose(t_y)
df = pd.DataFrame(t_y)
df.to_excel('.\\t_y.xlsx')
df.to_excel('.\\t_y2.xlsx', index=False)
df.to_excel('.\\t_y3.xlsx', index=False, header=None)
##
