##
import numpy as np
import loss_fun as lsf
import matplotlib.pyplot as plt

start, end, step = 0, 30, 0.5
x = np.arange(start, end + step, step)

step_w = float(input('请输入w的精度（eg:0.1）:'))
start_w, end_w = 0.5, 5
list_w = np.arange(start_w, end_w + step_w, step_w)

step_b = float(input('请输入b的精度（eg:0.1）:'))
print('运算中，请稍后……')

start_b, end_b = 0, 5
list_b = np.arange(start_b, end_b + step_b, step_b)

best_L, best_w, best_b, y2_end = float('inf'), 0, 0, 0

loop, i, j = 0, 0, 0
list_l = np.zeros((len(list_w), len(list_b)))
print(list_l)

for w in list_w:
    for b in list_b:
        y1 = x * w + b
        # print(type(y1))
        random_num = np.random.rand(1, len(y1)) * 2 - 1
        y2_m = y1.mean() * 0.20 * random_num
        y2 = y1 + y2_m
        # print(y2)
        L = lsf.loss_fun(y1, y2)
        list_l[i, j] = L
        # print(L)
        if L < best_L:
            best_L, best_w, best_b, y2_end = L, w, b, y2
        else:
            pass
        loop += 1
        j += 1
    i += 1
print(f'\nbest_L={best_L};\nbest_w={best_w};\nbest_b={best_b};\n循环次数={loop}.')

y1 = best_w * x + best_b  # 取得最佳y
y = 0.5 * x + 1  # 取得理论y

# 画图
'''画线'''
plt.plot(x, y1, c='#183E0C', label='best line')  # 实际
plt.plot(x, y, c='#000000', label='theory')  # 理论
plt.title("linear regression", fontsize=20)
plt.xlabel('x', fontsize=20)
plt.ylabel('y', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

'''画点'''
plt.plot(x, y2_end[0], linestyle='', marker='.', c='#0023F5', label='point')

plt.legend()
plt.show()

print(list_w, list_w, list_l)
print('\n运行结束')
##
