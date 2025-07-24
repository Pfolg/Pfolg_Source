# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   08_尝试获取QQ状态 |User    Pfolg
# 2024/7/13   11:14
import psutil

#获取全部进程的pid
pl = psutil.pids()
for pid in pl:
    # 判断QQ.exe是否运行
    if psutil.Process(pid).name() == "QQ.exe":
        print("QQ在线")
