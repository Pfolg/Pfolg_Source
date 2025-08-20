# -*- coding: UTF-8 -*-
"""
PROJECT_NAME ShuangPin
PRODUCT_NAME PyCharm
NAME main
AUTHOR Pfolg
TIME 2025/8/10 16:59
"""
import os
import socket
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QAction, QIcon
from PySide6.QtWidgets import QLabel, QWidget, QApplication, QFrame, QSystemTrayIcon, QMenu
from pynput import keyboard

"""pyinstaller --onefile --windowed --add-data "sp.png;." main.py"""


def resource_path(relative_path):
    """获取资源的绝对路径（兼容开发环境和打包后环境）"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


logo = resource_path("sp.png")

# 使用示例
ui_path = resource_path("typing.ui")
key_data = {
    # 自然码
    "Q": ["", "iu", ""],
    "W": ["", "ia", "ua"],
    "E": ["", "", ""],
    "R": ["", "uan", ""],
    "T": ["", "ue", "ve"],
    "Y": ["", "ing", "uai"],
    "U": ["sh", "", ""],
    "I": ["ch", "", ""],
    "O": ["", "uo", ""],
    "P": ["", "un", ""],
    # ---
    "A": ["", "", ""],
    "S": ["", "iong", "ong"],
    "D": ["", "iang", "uang"],
    "F": ["", "en", ""],
    "G": ["", "eng", ""],
    "H": ["", "ang", ""],
    "J": ["", "an", ""],
    "K": ["", "ao", ""],
    "L": ["", "ai", ""],
    # ---
    "Z": ["", "ei", ""],
    "X": ["", "ie", ""],
    "C": ["", "iao", ""],
    "V": ["zh", "ui", ""],
    "B": ["", "ou", ""],
    "N": ["", "in", ""],
    "M": ["", "ian", ""],
}


class MyKey(QLabel):
    def __init__(self, x: int, y: int, main_key: str, func_key: str, k1: str, k2: str, w=80):
        super().__init__()
        self.setGeometry(x, y, w, w)
        self.main_key = QLabel(main_key, self)
        self.func_key = QLabel(func_key, self)
        self.func_key.setStyleSheet("color:red;")
        self.k1 = QLabel(k1, self)
        self.k2 = QLabel(k2, self)
        font = QFont()
        font.setPointSize(16)
        self.main_key.setFont(font)
        self.setFrameShape(QFrame.Shape.Box)
        # 位置
        self.main_key.setGeometry(0, 0, int(w / 2), int(w / 2))
        self.func_key.setGeometry(int(w / 2), 0, int(w / 2), int(w / 2))
        self.k1.setGeometry(0, int(w / 2), int(w / 2), int(w / 2))
        self.k2.setGeometry(int(w / 2), int(w / 2), int(w / 2), int(w / 2))
        # 样式
        self.main_key.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.func_key.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.k1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.k2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(
            "color:#ffffff;"
            "background-color:rgba(12, 49, 110, 20)"
        )

        # 字体
        font.setPointSize(12)
        self.func_key.setFont(font)
        self.k1.setFont(font)
        self.k2.setFont(font)


class KWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 10*20*3 |-10 9*20 |-20 7*20 # 20->60px
        self.key_width = 80
        sw, sh = app.primaryScreen().geometry().width(), app.primaryScreen().geometry().height()
        w, h = 10 * self.key_width, 3 * self.key_width
        self.setGeometry(int((sw - w) / 2), int(sh - h - self.key_width), w, h)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowTransparentForInput |
            Qt.WindowType.ToolTip |
            Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        key_keys = list(key_data.keys())
        loc_x, loc_y = 0, 0
        for i in range(len(key_keys)):
            k = key_keys[i]
            a = MyKey(loc_x, loc_y, k, key_data.get(k)[0], key_data.get(k)[1], key_data.get(k)[2])
            a.setObjectName(k)
            a.setParent(self)
            if i == 9 or i == 18:
                loc_y += self.key_width
                loc_x = loc_y / 2
            else:
                loc_x += self.key_width

    @staticmethod
    def on_key_press(key):
        """处理键盘按下事件"""
        try:
            # 处理普通按键
            key_name = key.char.upper()
            print(key_name)
            k: MyKey = root.findChild(MyKey, key_name)
            k.setStyleSheet(
                "color:#ffffff;"
                "background-color:rgba(255, 208, 75, 80);"
            )
        except Exception as e:
            print(str(e))
            return

    @staticmethod
    def on_key_release(key):
        """处理键盘释放事件"""
        try:
            # 处理普通按键
            key_name = key.char.upper()
            print(key_name)
            k: MyKey = root.findChild(MyKey, key_name)
            k.setStyleSheet(
                "color:#ffffff;"
                "background-color:rgba(12, 49, 110, 20)"
            )
        except Exception as e:
            print(str(e))
            return


def single_instance(port: int):
    try:
        # 选择一个不常用的端口
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", port))
    except socket.error:
        print("另一个实例正在运行，退出。")
        sys.exit(1)
    return sock


class Tray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.menu = QMenu()
        ac_q = QAction("Quit", self.menu)
        ac_q.triggered.connect(sys.exit)
        self.menu.addAction(ac_q)
        self.setContextMenu(self.menu)
        self.setIcon(QIcon(logo))
        self.setToolTip("双拼练习辅助工具")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont("Maple Mono NF CN Medium")
    root = KWindow()
    root.show()
    keyboardListener = keyboard.Listener(on_press=root.on_key_press, on_release=root.on_key_release)
    keyboardListener.start()
    t = Tray()
    ins = single_instance(7086)
    sys.exit(app.exec())
