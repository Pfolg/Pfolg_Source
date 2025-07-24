# -*- coding: utf-8 -*-
# Project >>> make_pie.py   ||    Environment >>> PyCharm
# FileName >>> 53_文件查找与选择    ||    Author >>> Pfolg
# Date >>> 2024/6/16 and Time >>> 19:15
import tkinter as tk
from tkinter import filedialog

# 实例化
root = tk.Tk()
root.withdraw()

# 获取文件夹路径
f_path = filedialog.askopenfilename()  # 可加s
print('\n获取的文件地址：', f_path)
