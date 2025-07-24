# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""

from PyQt6.QtWidgets import QApplication, QPushButton, QDialog, QFontDialog, QColorDialog
import sys
from PyQt6 import uic


def select_font():
    font, ok = QFontDialog.getFont()
    if ok:
        print(font)


def select_color():  # 只会返回颜色
    # 弹出颜色对话框并获取颜色
    color = QColorDialog.getColor()

    if color.isValid():
        # 获取颜色信息
        hex_color = color.name()  # 十六进制字符串，如 "#ff0000"
        rgb = color.getRgb()  # 元组 (R, G, B, A)
        rgba_normalized = color.getRgbF()  # 浮点数元组 (0-1范围)

        print(f"十六进制: {hex_color}")
        print(f"RGB(A) 值: {rgb}")
        print(f"标准化 RGBA: {rgba_normalized}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    pushButton: QPushButton = ui.pushButton
    pushButton2: QPushButton = ui.pushButton_2
    print(pushButton.text(), pushButton2.text())
    pushButton.clicked.connect(select_font)
    pushButton2.clicked.connect(select_color)
    ui.show()
    sys.exit(app.exec())
