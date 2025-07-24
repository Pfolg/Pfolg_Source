# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from operator import index

from PyQt6.QtCore import QDate, QTime
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QToolBox, QWidget, QDateTimeEdit
import sys
from PyQt6 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui2.ui")
    # dateTimeEdit: QDateTimeEdit = ui.dateTimeEdit
    # dateTimeEdit.setDate(QDate(2025, 2, 28))
    # dateTimeEdit.setTime(QTime(23, 59, 59))
    # print(dateTimeEdit.dateTime().toString("yyyy/M/d H:mm:ss"))
    ui.show()
    sys.exit(app.exec())
