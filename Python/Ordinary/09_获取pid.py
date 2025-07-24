# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   09_获取pid |User    Pfolg
# 2024/7/13   17:38
import psutil


def get_pid_by_name(process_name):
    pid = None
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == process_name:
            pid = proc.info['pid']
            break
    return pid


process_name = 'QQ.exe'
pid = get_pid_by_name(process_name)
if pid is not None:
    print(f"The PID of process {process_name} is {pid}")
else:
    print(f"No process named {process_name} is found")