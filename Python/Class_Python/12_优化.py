##
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter

# 建立表格
# y = np.linspace(10, 0, 21)
# h0 = 10
# g = 9.8
# t = np.sqrt(2 * (h0 - y) / g)
#
# t_y = np.vstack((t, y))
# t_y = np.transpose(t_y)
# df = pd.DataFrame(t_y)
# df.to_excel('.\\t_y.xlsx')
# df.to_excel('.\\t_y2.xlsx', index=False)
# df.to_excel('.\\t_y3.xlsx', index=False, header=None)

# 读表
df = pd.read_excel('.\\t_y3.xlsx', index_col=None, header=None)
array = df.to_numpy()
print(array)

# 处理数据
phot_t = array[:, 0]
phot_y = array[:, 1]
print()
print('phot_x=', phot_t, '\n', 'phot_y=', phot_y)  # 验证数据采集正确

# 画图
plt.plot(phot_t, phot_y, c='#377D22')
plt.title("y-t guan_xi_tu y0=10", fontsize=20)
plt.xlabel('time', fontsize=20)
plt.ylabel('position', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.show()

# 验证程序运行结束
print('end')

# 花里胡哨
# win = tkinter.Tk()
# win.config(bg='#ffffff')
# screenwidth = win.winfo_screenwidth()  # 获取屏幕宽度
# screenheight = win.winfo_screenheight()  # 获取屏幕长度
# width, height = 1024, 512  # 设置窗口长宽
# size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
# win.geometry(size_geo)  # 设置窗口属性
# win.title('花里胡哨')
# L = tkinter.Label(win, text='end')
# L.pack()
# win.mainloop()
##
