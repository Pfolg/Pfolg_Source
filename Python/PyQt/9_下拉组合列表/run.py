# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtGui import QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QTextEdit, QFrame, QComboBox, QLCDNumber, \
    QToolButton, QCheckBox
import sys
from PyQt6 import uic, QtGui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    comboBox: QComboBox = ui.comboBox
    comboBox.addItem("嗨喽")
    items = ["你好", "hello", "good"]
    comboBox.addItems(items)

    comboBox.addItem(
        QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\comment-dots.svg"),
        "message")
    print(comboBox.currentText(), comboBox.currentIndex())
    print(comboBox.itemText(2), comboBox.count())
    comboBox.setCurrentText("good")  # 从已有的中设置当前选中
    print(comboBox.currentIndex())
    ui.show()
    sys.exit(app.exec())
