# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QTextEdit, QFrame, QComboBox, QLCDNumber, \
    QToolButton
import sys
from PyQt6 import uic, QtGui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    ui.show()
    toolButton: QToolButton = ui.toolButton
    toolButton.setVisible(False)
    sys.exit(app.exec())
