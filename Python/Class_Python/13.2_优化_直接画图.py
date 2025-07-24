import numpy
import random
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

# 画图
'''画线'''
plt.plot(line_x, line_y, c='#000000')
plt.title("this is a label", fontsize=20)
plt.xlabel('x', fontsize=20)
plt.ylabel('y', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

'''画点'''
plt.plot(line_x, nose, linestyle='', marker='.', c='#FF0000')

plt.show()

print('\n运行结束')
