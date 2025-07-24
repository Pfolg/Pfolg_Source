# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""

from PyQt6.QtWidgets import QApplication, QPushButton, \
    QMessageBox
import sys
from PyQt6 import uic


def show_Message():
    # QMessageBox.information(
    #     ui, "title", "消息对话框", QMessageBox.StandardButton.Ok,
    #     QMessageBox.StandardButton.Cancel)
    # QMessageBox.information(
    #     ui, "title", "消息对话框", QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Cancel)
    # QMessageBox.information(
    #     ui, "title", "消息对话框", QMessageBox.StandardButton.Abort,
    #     QMessageBox.StandardButton.Cancel)
    # QMessageBox.information(
    #     ui, "title", "消息对话框", QMessageBox.StandardButton.Ignore,
    #     QMessageBox.StandardButton.Help)
    result = QMessageBox.information(
        ui, "title", "消息对话框", QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.Yes)
    if result == QMessageBox.StandardButton.Yes:
        print("yes")
    else:
        print("No")


def show_Error():
    QMessageBox.critical(
        ui, "title", "错误对话框", QMessageBox.StandardButton.Ok,
        QMessageBox.StandardButton.Cancel)


def show_Question():
    QMessageBox.question(
        ui, "title", "问答对话框", QMessageBox.StandardButton.Ok,
        QMessageBox.StandardButton.Cancel)


def show_About():
    QMessageBox.about(ui, "title", "关于对话框")  # 不能加按钮


def show_Warning():
    QMessageBox.warning(
        ui, "title", "警告对话框", QMessageBox.StandardButton.Ok,
        QMessageBox.StandardButton.Cancel)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    pushButton_2: QPushButton = ui.pushButton_2
    pushButton_2.clicked.connect(show_Message)
    pushButton_3: QPushButton = ui.pushButton_3
    pushButton_3.clicked.connect(show_Error)
    pushButton: QPushButton = ui.pushButton
    pushButton.clicked.connect(show_Question)
    pushButton_5: QPushButton = ui.pushButton_5
    pushButton_5.clicked.connect(show_About)
    pushButton_4: QPushButton = ui.pushButton_4
    pushButton_4.clicked.connect(show_Warning)
    ui.show()
    sys.exit(app.exec())
