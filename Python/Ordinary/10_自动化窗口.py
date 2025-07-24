# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   10_自动化窗口 |User    Pfolg
# 2024/7/13   17:53
# article https://blog.csdn.net/qq_39147299/article/details/132409817
import time

import psutil
from pywinauto import application

"""
求学之路免不了失败
"""

def get_pid_by_name(process_name):
    pid = None
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == process_name:
            pid = proc.info['pid']
            break
    return pid


processName = "QQ.exe"
pid = get_pid_by_name(processName)
print(pid)
app = application.Application().connect(process=pid)
QQWindow = app["一亩三分地"]
QQWindow.print_control_identifiers()
"""
# 选择控件的方法
wind_calc = app["窗口名"]["控件名"]
"""
dlg = app.root(title="一亩三分地")
# dlg = app.window(title="微信")
print("get_show_state:", dlg.get_show_state())  # 2 获取窗口状态，0正常1最大化2最小化
print("was_maximized:", dlg.was_maximized())  # False
dlg.print_control_identifiers()
time.sleep(1)
print("-" * 50)
dlg.draw_outline()  # 给窗口画个框以便定位
time.sleep(1)
dlg.maximize()
time.sleep(1)
dlg.restore()
time.sleep(1)
dlg.minimize()
# dlg.close()


# dlg = app.window(class_name="TXGuiFoundation")
# list_data = dlg.child_window(title="聊天", control_type="List")
# for item in list_data:
#     print(type(item))
#     element_info = item.element_info
#     print(type(element_info))
#     print("window_text:", )
#     print("rich_text:", element_info.rich_text)
#     print("name:", element_info.name)
#     print("visible:", element_info.visible)
#     print("rectangle:", element_info.rectangle)
#     print("class_name:", element_info.class_name)
#     print("enabled:", element_info.enabled)
#     print("parent:", element_info.parent)
#     print("children:", element_info.children())
#     print("iter_children:", element_info.iter_children())
#     if item.window_text() == "文件传输助手":
#         item.click_input()
#         item.type_keys("冰冷的希望")
#         item.type_keys("{VK_RETURN}")
#     print()

dlg.print_control_identifiers()
message_button = dlg.child_window(title="聊天", control_type="Button")
print(message_button)
