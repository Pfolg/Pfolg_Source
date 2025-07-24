# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QTextEdit, QFrame, QComboBox, QLCDNumber
import sys
from PyQt6 import uic, QtGui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    ui.show()
    frame1: QFrame = ui.frame
    frame1.setVisible(True)
    label_3: QLabel = ui.label_3
    label_3.setText("文本选择框")
    comboBox: QComboBox = ui.comboBox
    comboBox.addItems(["我是程序员", "她是学霸", "PyCharm——YYDS", "用来凑数的选项"])

    lcdNumber: QLCDNumber = ui.lcdNumber
    print(lcdNumber.intValue(), lcdNumber.value())
    lcdNumber.setProperty("value", 6.66)

    sys.exit(app.exec())
