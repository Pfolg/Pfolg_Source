# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""

from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QSpacerItem, QDial, QScrollBar, QPushButton, \
    QFileDialog
import sys
from PyQt6 import uic


def select_file():
    fd = QFileDialog()
    fd.setFileMode(QFileDialog.FileMode.ExistingFiles)  # 设置文件多选
    # fd.setDirectory("C:/")  # 设置初始路径
    # fd.getExistingDirectory()
    fd.setNameFilter("*.jpg *.png *.py *.ui")
    fd.setViewMode(QFileDialog.ViewMode.List)  # QFileDialog.ViewMode.Detail
    # fd.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)# 默认：打开模式/保存模式
    if fd.exec():
        print(fd.selectedFiles())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    pushButton: QPushButton = ui.pushButton
    pushButton.clicked.connect(select_file)
    ui.show()
    sys.exit(app.exec())
