# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QSpacerItem, QDial, QScrollBar, QLineEdit, \
    QPushButton, QInputDialog
import sys


# from PyQt6 import uic


def getName(formLayoutWidget, box: QLineEdit):
    r1, r2 = QInputDialog.getText(
        formLayoutWidget, "姓名", "请输入姓名", QLineEdit.EchoMode.Normal,
        text="name0")  # PasswordEchoOnEdit
    if r2:
        box.setText(r1)


def getClass(formLayoutWidget, box: QLineEdit):
    r1, r2 = QInputDialog.getItem(formLayoutWidget, "班级", "请选择班级：", ("1", "2", "3", "4"), 0, editable=False)
    if r2:
        box.setText(r1)


def getAge(formLayoutWidget, box: QLineEdit):
    r1, r2 = QInputDialog.getInt(
        formLayoutWidget, "年龄", "请输入年龄", value=18, min=1, max=100, step=1)  # PasswordEchoOnEdit
    # print(r)
    if r2:
        box.setText(str(r1))


def getGrade(formLayoutWidget, box: QLineEdit):
    r1, r2 = QInputDialog.getDouble(
        formLayoutWidget, "成绩", "请输入成绩", value=60, decimals=2)  # PasswordEchoOnEdit
    if r2:
        box.setText(str(r1))


def inputInfor(args: list):
    for i in args:
        print(i.text(), end=" ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    faW = ui.formLayoutWidget
    lineEdit_name: QLineEdit = ui.lineEdit
    lineEdit_age: QLineEdit = ui.lineEdit_2
    lineEdit_class: QLineEdit = ui.lineEdit_3
    lineEdit_grade: QLineEdit = ui.lineEdit_4
    pushButton: QPushButton = ui.pushButton

    lineEdit_name.returnPressed.connect(lambda: getName(faW, lineEdit_name))
    lineEdit_age.returnPressed.connect(lambda: getAge(faW, lineEdit_age))
    lineEdit_class.returnPressed.connect(lambda: getClass(faW, lineEdit_class))
    lineEdit_grade.returnPressed.connect(lambda: getGrade(faW, lineEdit_grade))

    pushButton.clicked.connect(lambda: inputInfor([lineEdit_name, lineEdit_age, lineEdit_class, lineEdit_grade]))

    ui.show()
    sys.exit(app.exec())
