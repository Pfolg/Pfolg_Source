# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from operator import index

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QToolBox, QWidget
import sys
from PyQt6 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    toolBox: QToolBox = ui.toolBox
    tab1 = QWidget()
    toolBox.insertItem(
        2, tab1,
        QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\file-code.svg"),
        "Python")  # 添加选项卡
    toolBox.setCurrentIndex(1)  # 选中第二个选项卡
    toolBox.setItemToolTip(3, "这是提示")  # 设置提示
    toolBox.setItemIcon(4, QIcon(
        r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\life-ring.svg"))  # 设置图标
    toolBox.setItemText(0, "Pycharm")
    toolBox.setItemText(4, "Vpet")
    toolBox.setItemEnabled(2, False)  # 使第三个选项卡不可用
    # toolBox.removeItem(3)  # 会影响布局，不好用
    ui.show()
    sys.exit(app.exec())
