# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   12_通知 |User    Pfolg
# 2024/8/5   13:26
from plyer import notification


notification.notify(
    title='提醒',
    message="Hello World",
    timeout=10,  # 通知显示时间，单位为秒
    # app_icon=r"D:\PycharmProjects\pythonProject\Box\resource\ico.ico"
)
#########################################################
from win10toast import ToastNotifier

# 创建一个通知对象
toaster = ToastNotifier()

# 显示一个自定义标题的通知
toaster.show_toast("自定义标题", "这是通知的内容", duration=10)
