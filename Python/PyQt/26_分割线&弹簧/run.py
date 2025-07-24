# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QSpacerItem, QDial, QScrollBar
import sys
from PyQt6 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    # spacerItem: QSpacerItem = ui.spacerItem
    # print(spacerItem, "is 弹簧")
    dial: QDial = ui.dial
    print(dial, "是旋钮")
    horizontalScrollBar: QScrollBar = ui.horizontalScrollBar  # 滚动条
    ui.show()
    sys.exit(app.exec())
