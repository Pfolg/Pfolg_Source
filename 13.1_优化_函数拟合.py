'''
import numpy

ar7 = numpy.random.random((5, 6))
print(ar7, '\n')

i = ar7[1, :]
j = ar7[:, 3]
k = ar7[3, 0:3]
l = ar7[4:6, 4]
print(f'{i}\n{j}\n{k}\n{l}')
'''

import numpy
import random
import pandas
import matplotlib.pyplot as plt

# 直线
line_x = numpy.arange(0, 30.5, step=0.5)
m_list = []
# print(line_x)
for i in range(len(line_x)):
    m_y = line_x[i] * 2 + 1
    m_list.append(m_y)
line_y = numpy.array(m_list)
# print(line_y)

# 生成数据
list_nose = []
for j in range(len(line_y)):
    random_vector = random.uniform(a=-1, b=1)
    # print(random_vector)
    noise_m = line_y[j] + random_vector * 5
    list_nose.append(noise_m)
nose = numpy.array(list_nose)

# 将数据添加到表格
ns = numpy.vstack((line_x, nose))
ns = numpy.transpose(ns)
excel_nose = pandas.DataFrame(ns)
excel_nose.to_excel('.\\nose.xlsx', index=False, header=None)

# 读表
df = pandas.read_excel('.\\nose.xlsx', index_col=None, header=None)
array_use = df.to_numpy()
# print(array_use)

# 处理数据
phot_num = array_use[:, 0]
phot_y = array_use[:, 1]
# print()
# print('phot_x=', phot_num, '\n', 'phot_y=', phot_y)  # 验证数据采集正确

# 画图
'''画线'''
plt.plot(line_x, line_y, c='#000000')
plt.title("this is a label", fontsize=20)
plt.xlabel('x', fontsize=20)
plt.ylabel('y', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

'''画点'''
plt.plot(phot_num, phot_y, linestyle='', marker='.', c='#FF0000')

plt.show()

print('\n运行结束')