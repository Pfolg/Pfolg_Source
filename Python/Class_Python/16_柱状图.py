# 频率分布直方图 均匀分布
import numpy as np
import matplotlib.pyplot as plt

uni=np.random.random(10000)
fig, ax = plt.subplots()
plt.hist(uni, bins=20, color='b', edgecolor='k', linewidth=1.5)
plt.xlabel('b', fontsize=20)
plt.ylabel('Number', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.show()