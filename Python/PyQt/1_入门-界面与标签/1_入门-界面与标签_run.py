# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME 1_入门-界面与标签
AUTHOR Pfolg
TIME 2025/2/26 18:57
"""
from PyQt6.QtWidgets import QApplication
import sys
from PyQt6 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./1_入门-界面与标签.ui")
    ui.show()
    sys.exit(app.exec())
