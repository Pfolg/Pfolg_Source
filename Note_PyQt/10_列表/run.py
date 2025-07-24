# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from operator import index

from PyQt6.QtGui import QIntValidator, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QTextEdit, QFrame, QComboBox, QLCDNumber, \
    QToolButton, QCheckBox, QListWidget, QListWidgetItem
import sys
from PyQt6 import uic, QtGui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    listWidget: QListWidget = ui.listWidget
    listWidget.addItems(["1", "2", "3", "4"])
    listItem = QListWidgetItem()
    listItem.setIcon(QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\compass.svg"))
    listItem.setToolTip("This is a description.")
    listItem.setText("Test")
    listWidget.addItem(listItem)
    listWidget.addItem("你好，李焕英")
    # listWidget.insertItem(0, listItem)
    print(listWidget.selectedItems())
    ui.show()
    sys.exit(app.exec())
