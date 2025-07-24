# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QTextEdit
import sys
from PyQt6 import uic, QtGui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    ui.show()
    textEdit1: QTextEdit = ui.textEdit
    textEdit2: QTextEdit = ui.textEdit_2
    label1: QLabel = ui.label
    label2: QLabel = ui.label_2
    label1.setText("这是纯文本")

    textEdit1.setTextColor(QtGui.QColor("#2167cb"))
    textEdit1.setTextBackgroundColor(QtGui.QColor("#d55fde"))
    textEdit1.setPlainText("我大概是病了，不知道死期何日何时，不过我还是期待它早一点来临，不至于让我受太多苦。")
    textEdit2.setMarkdown("# P1\n本文的主旨是——")
    textEdit1.setVisible(True)
    print(textEdit1.toPlainText(), textEdit2.toMarkdown())

    # textEdit1.clear()
    # textEdit2.clear()
    sys.exit(app.exec())
