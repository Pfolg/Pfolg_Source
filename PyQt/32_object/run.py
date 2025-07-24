# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""

from PyQt6.QtWidgets import QApplication, QLabel
import sys
from PyQt6 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    with open("label.qss", "r") as f:
        app.setStyleSheet(f.read())  # 更改标签2样式

    label: QLabel = ui.label
    label2: QLabel = ui.label_2
    label3: QLabel = ui.label_3
    label.setProperty("level", "warning")
    label2.setProperty("level", "error")
    label3.setProperty("level", "error")

    ui.show()
    sys.exit(app.exec())
