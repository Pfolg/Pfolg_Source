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
    QToolButton, QCheckBox, QListWidget, QListWidgetItem, QTabWidget
import sys
from PyQt6 import uic, QtGui, QtWidgets

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    tabWidget: QTabWidget = ui.tabWidget
    tabWidget.addTab(QTabWidget(), "404")
    added = QTabWidget()
    groupBox = QtWidgets.QGroupBox(parent=added)
    groupBox.setTitle("标签add打组")
    groupBox.setBaseSize(100, 100)
    tabWidget.insertTab(0, added, "test")
    tabWidget.setCurrentIndex(0)
    tabWidget.setTabText(0, "嗨害嗨")
    # tabWidget.setCornerWidget(added)
    # tabWidget.setCornerWidget()
    ui.show()
    sys.exit(app.exec())
