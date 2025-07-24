# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
import threading
import time

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMenuBar, QMenu, QStyle, QMainWindow, QToolBar, QStatusBar, QLabel, \
    QProgressBar
import sys
from PyQt6 import uic, QtCore

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")

    ui.show()
    sys.exit(app.exec())
