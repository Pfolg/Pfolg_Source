# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""

from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton
import sys
from PyQt6 import uic


def ca(l1: QLineEdit, l2: QLineEdit, l3: QLineEdit):
    if l1.text() and l2.text():
        l3.setText(str(int(l1.text()) + int(l2.text())))


def style(l: QLineEdit):
    l.setStyleSheet("background-color:#25EB28")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    lineEdit: QLineEdit = ui.lineEdit
    lineEdit2: QLineEdit = ui.lineEdit_2
    lineEdit3: QLineEdit = ui.lineEdit_3
    lineEdit3.setVisible(False)

    pushButton: QPushButton = ui.pushButton
    pushButton.clicked.connect(lambda: ca(lineEdit, lineEdit2, lineEdit3))
    pushButton.clicked.connect(lambda: style(lineEdit3))  # 两个槽函数监听一个信号

    ui.show()
    sys.exit(app.exec())
