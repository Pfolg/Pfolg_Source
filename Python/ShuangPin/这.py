# -*- coding: UTF-8 -*-
"""
PROJECT_NAME aiChange.py
PRODUCT_NAME PyCharm
NAME 这
AUTHOR Pfolg
TIME 2025/8/11 20:44
"""
# -*- coding: UTF-8 -*-
"""
PROJECT_NAME ShuangPin
PRODUCT_NAME PyCharm
NAME main
AUTHOR Pfolg
TIME 2025/8/10 16:59
"""
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QWidget, QApplication, QFrame

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
        self.setStyleSheet("color:#89ca78;background-color:rgba(12, 49, 110, 20)")

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
            a.setParent(self)
            if i == 9 or i == 18:
                loc_y += self.key_width
                loc_x = loc_y / 2
            else:
                loc_x += self.key_width


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont("Maple Mono NF CN Medium")
    root = KWindow()
    root.show()
    sys.exit(app.exec())
