import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 读取数据
my_num = pd.read_excel('.\\x_pdf.xlsx', index_col=None, header=None)
num = my_num.to_numpy()
x = num[:, 0]
PDF = num[:, 1]
# print(x, PDF)

# PDF曲线
fig, ax = plt.subplots()
plt.plot(x, PDF, color='r', linewidth=4.0)
plt.xlabel('x', fontsize=20)
plt.ylabel('PDF', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.show()

# CDF曲线
cdf = np.zeros(len(PDF))
for i in range(len(PDF)):
    cdf[i] = np.trapz(PDF[0:i])
cdf = cdf / cdf.max()
plt.plot(x, cdf, color='r', linewidth=4.0)
plt.xlabel('x', fontsize=20)
plt.ylabel('CDF', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.show()
