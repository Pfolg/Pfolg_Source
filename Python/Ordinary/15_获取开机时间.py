# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   15_获取开机时间 |User    Pfolg
# 2024/10/20 00:30
import subprocess


def get_uptime_windows():
    # 使用 systeminfo 命令获取系统信息
    result = subprocess.run(["systeminfo"], capture_output=True, text=True)
    # 系统信息中包含开机时间
    for line in result.stdout.splitlines():
        if "System Boot Time" in line:
            boot_time_str = line.split(",")[1].strip()
            return boot_time_str, line
    return "无法获取开机时间"


# 使用函数
uptime = get_uptime_windows()
print("本次开机已使用时间:", uptime)
