# -*- coding: UTF-8 -*-
import os
import socket
import sys

from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont, QAction, QIcon
from PySide6.QtWidgets import QLabel, QWidget, QApplication, QFrame, QSystemTrayIcon, QMenu
from pynput import keyboard


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


logo = resource_path("sp.png")

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


class KeyboardListener(QThread):
    key_pressed = Signal(str)
    key_released = Signal(str)

    def run(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release
        ) as listener:
            listener.join()

    def on_press(self, key):
        try:
            if hasattr(key, 'char') and key.char:
                self.key_pressed.emit(key.char.upper())
        except Exception as e:
            print(f"Press error: {e}")

    def on_release(self, key):
        try:
            if hasattr(key, 'char') and key.char:
                self.key_released.emit(key.char.upper())
        except Exception as e:
            print(f"Release error: {e}")


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

        self.main_key.setGeometry(0, 0, int(w / 2), int(w / 2))
        self.func_key.setGeometry(int(w / 2), 0, int(w / 2), int(w / 2))
        self.k1.setGeometry(0, int(w / 2), int(w / 2), int(w / 2))
        self.k2.setGeometry(int(w / 2), int(w / 2), int(w / 2), int(w / 2))

        self.main_key.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.func_key.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.k1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.k2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setStyleSheet(
            "color:#ffffff;"
            "background-color:rgba(171, 111, 200, 50)"
        )

        font.setPointSize(12)
        self.func_key.setFont(font)
        self.k1.setFont(font)
        self.k2.setFont(font)


class KWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.key_width = 80
        screen = QApplication.primaryScreen().geometry()
        w, h = 10 * self.key_width, 3 * self.key_width
        self.setGeometry(
            int((screen.width() - w) / 2),
            int(screen.height() - h - self.key_width),
            w, h
        )
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowTransparentForInput |
            Qt.WindowType.ToolTip |
            Qt.WindowType.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        key_keys = list(key_data.keys())
        loc_x, loc_y = 0, 0
        for i, k in enumerate(key_keys):
            a = MyKey(loc_x, loc_y, k, key_data[k][0], key_data[k][1], key_data[k][2], self.key_width)
            a.setParent(self)
            a.setObjectName(k)

            if i in [9, 18]:  # 行尾换行
                loc_y += self.key_width
                loc_x = loc_y / 2
            else:
                loc_x += self.key_width

        # 创建并启动键盘监听线程
        self.listener_thread = KeyboardListener()
        self.listener_thread.key_pressed.connect(self.handle_key_press)
        self.listener_thread.key_released.connect(self.handle_key_release)
        self.listener_thread.start()

    def handle_key_press(self, key_name):
        """处理按键按下事件（UI线程安全）"""
        key_widget = self.findChild(MyKey, key_name)
        if key_widget:
            key_widget.setStyleSheet(
                "color:#ffffff;"
                "background-color:rgba(255, 208, 75, 80);"
            )

    def handle_key_release(self, key_name):
        """处理按键释放事件（UI线程安全）"""
        key_widget = self.findChild(MyKey, key_name)
        if key_widget:
            key_widget.setStyleSheet(
                "color:#ffffff;"
                "background-color:rgba(171, 111, 200, 50)"
            )


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


def single_instance(port: int):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", port))
        return sock
    except socket.error:
        print("另一个实例正在运行，退出。")
        sys.exit(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont("Maple Mono NF CN Medium")

    # 确保单实例运行
    instance_lock = single_instance(7086)

    window = KWindow()
    window.show()

    tray = Tray()

    sys.exit(app.exec())
