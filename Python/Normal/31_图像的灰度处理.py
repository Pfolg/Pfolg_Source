import numpy as np
import matplotlib.pyplot as plt

n1 = plt.imread('google.png')
print(n1, type(n1))  # 三维数组，最高维度表示图像的高，次高维度表示宽，最低维度表示RGB
plt.imshow(n1)

# 编写灰度公式
n2 = np.array([0.299, 0.587, 0.114])
# 将n1与n2灰度公式进行点乘运算
x = np.dot(n1, n2)
# 传入数组，显示灰度
plt.imshow(x, cmap='gray')

plt.show()
