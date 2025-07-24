# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:18:17 2024

@author: YANG_N
"""

import numpy as np
import matplotlib.pyplot as plt

# 频率分布直方图 - 均匀分布
uniform_values = np.random.random(10000)
fig, ax = plt.subplots()
plt.hist(uniform_values, bins=20, color='b', edgecolor='k', linewidth=1.5)
plt.xlabel('x', fontsize=20)
plt.ylabel('Number', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.show()

# 概率密度曲线 - 均匀分布
from scipy.stats import uniform

lower_a = 0
upper_b = 1
x = np.linspace(0, 1, 1000)
uniform_pdf = uniform.pdf(x, lower_a, upper_b - lower_a)
fig, ax = plt.subplots()
plt.plot(x, uniform_pdf, color='r', linewidth=4.0)
plt.xlabel('x', fontsize=20)
plt.ylabel('PDF', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.ylim(0, 1.1)
plt.show()

# 频率分布直方图 - 高斯分布
normal_values = np.random.normal(loc=80, scale=5, size=1000)
fig, ax = plt.subplots()
plt.hist(normal_values, bins=20, color='b', edgecolor='k', linewidth=1.5)
plt.xlabel('Score', fontsize=20)
plt.ylabel('PDF', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlim(60, 100)
plt.show()

# 概率密度曲线 - 高斯分布
from scipy.stats import norm

mean = 80
std = 5
x = np.linspace(60, 100, 1000)
normal_pdf = norm.pdf(x, mean, std)
fig, ax = plt.subplots()
plt.plot(x, normal_pdf, color='r', linewidth=4.0)
plt.xlabel('Score', fontsize=20)
plt.ylabel('PDF', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.show()
