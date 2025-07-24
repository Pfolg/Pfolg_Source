# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMenuBar, QMenu, QStyle, QMainWindow, QToolBar, QStatusBar, QLabel
import sys
from PyQt6 import uic, QtCore


def exitui():
    ui.destroy()
    sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")

    statusbar: QStatusBar = ui.statusbar
    标签1 = QLabel("Status Bar")
    标签2 = QLabel("mail：4654646449684@gmail.com")
    statusbar.addWidget(标签1)
    statusbar.addWidget(标签2)
    statusbar.addPermanentWidget(QLabel("This is a test window"))

    statusbar.removeWidget(标签1)
    statusbar.removeWidget(标签2)
    statusbar.showMessage("当前学习进度：60%", 5000)  # ms
    ui.show()

    sys.exit(app.exec())
