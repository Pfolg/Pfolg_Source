"""
Project    makeFilesPhot.py |Environment    PyCharm
File_name   03_AI给的待办事项项目 |User    Pfolg
2024/7/7   15:30
"""
import tkinter as tk
from tkinter import messagebox

# 待办事项列表
todos = []


# 添加待办事项
def add_todo():
    todo_text = entry.get()
    if todo_text:
        todos.append(todo_text)
        listbox.insert(tk.END, todo_text)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("警告", "待办事项不能为空！")


# 删除待办事项
def delete_todo():
    selected = listbox.curselection()
    if selected:
        todos.pop(selected[0])
        listbox.delete(selected[0])


# 创建主窗口
root = tk.Tk()
root.title("待办事项列表")

# 创建输入框和按钮
entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=10, pady=10)

button_add = tk.Button(root, text="添加", command=add_todo)
button_add.pack(side=tk.LEFT, padx=10, pady=10)

button_delete = tk.Button(root, text="删除", command=delete_todo)
button_delete.pack(side=tk.LEFT, padx=10, pady=10)

# 创建列表框
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(side=tk.LEFT, padx=10, pady=10)

# 运行主循环
root.mainloop()
