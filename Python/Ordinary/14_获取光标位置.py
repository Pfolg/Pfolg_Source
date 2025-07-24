# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   14_获取光标位置 |User    Pfolg
# 2024/8/22   9:21
import tkinter as tk


def get_cursor_position(event):
    print("光标位置:", event.x, event.y)


root = tk.Tk()
text_area = tk.Text(root)
text_area.pack()

text_area.bind("<Motion>", get_cursor_position)

root.mainloop()
