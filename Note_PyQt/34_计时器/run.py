# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtCore import QTimer, QDateTime
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton
import sys
from PyQt6 import uic


def show(l):
    t = QDateTime.currentDateTime()

    td = t.toString("yyyy/MM/dd HH:mm:ss")
    l.setText(td)


def stop(t: QTimer):
    t.stop()


def start_time(t, l):
    t.start(500)
    t.timeout.connect(lambda: show(l))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    pushButton: QPushButton = ui.pushButton
    pushButton2: QPushButton = ui.pushButton_2
    label: QLabel = ui.label
    timer = QTimer(ui)
    pushButton.clicked.connect(lambda: start_time(timer, label))
    pushButton2.clicked.connect(lambda: stop(timer))
    ui.show()
    sys.exit(app.exec())
