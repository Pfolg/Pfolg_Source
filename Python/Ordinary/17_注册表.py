# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   17_注册表 |User    Pfolg
# 2024/10/25 12:56
import winreg as reg

# 定义注册表路径和值
key_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced'
value_name = 'HideIcons'
value_data = 1# 0

# 打开注册表键
try:
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_WRITE)
    # 设置值
    reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value_data)
    # 关闭注册表键
    reg.CloseKey(key)
    print("桌面图标已隐藏。")
except Exception as e:
    print(f"发生错误：{e}")

# 这段代码会将HideIcons的值设置为1，这通常会隐藏桌面图标。如果你想要恢复显示桌面图标，可以将value_data设置为0


"""
import winreg as reg

# 定义注册表路径和值名称
key_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced'
value_name = 'HideIcons'

# 打开注册表键
try:
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_READ)
    # 获取值
    value_data, value_type = reg.QueryValueEx(key, value_name)
    # 关闭注册表键
    reg.CloseKey(key)
    print(f"获取到的 {value_name} 值为: {value_data}", value_type)
except Exception as e:
    print(f"获取 {value_name} 时发生错误：{e}")
"""