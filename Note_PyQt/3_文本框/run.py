# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton
import sys
from PyQt6 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    ui.show()
    x0: QLabel = ui.label_2
    x0.setText("Windows 11 welcomes you!")
    x: QLineEdit = ui.lineEdit  # 类型注释
    x2: QLineEdit = ui.lineEdit_2  # 类型注释
    x2.setValidator(QIntValidator())  # 只能输入整数
    print(x.text())
    x.clear()
    print("文本已清除")
    x.setText("这是重新设定后的文本")
    x.clear()
    btu: QPushButton = ui.pushButton
    # btu.
    sys.exit(app.exec())
