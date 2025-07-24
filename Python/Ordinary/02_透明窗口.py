# -*- coding: utf-8 -*-
# Project >>> make_files.py   ||    Environment >>> PyCharm
# FileName >>> 02_透明窗口    ||    Author >>> Pfolg
# Date >>> 2024/6/30 and Time >>> 22:34
from tkinter import *

# 使窗口透明区不可交互
# 如果只想使窗口的某个部分透明，例如标题栏或侧边栏，那么该如何实现呢？我们可以使用WM_ATTRIBUTES属性。
root = Tk()

# 设置500x500窗口的位置和大小
root.geometry("500x500+200+200")

# 设置窗口属性
root.overrideredirect(1)
root.attributes('-alpha', 0.5)
root.attributes("-transparent", "blue")

# 绘制一个红色矩形
canvas = Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_rectangle(150, 100, 350, 400, fill="red")

root.mainloop()
