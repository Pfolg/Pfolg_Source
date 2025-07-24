# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
import threading
import time

from PyQt6.QtGui import QAction, QIcon, QStandardItemModel, QFileSystemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QMenuBar, QMenu, QStyle, QMainWindow, QToolBar, QStatusBar, QLabel, \
    QProgressBar, QTreeView
import sys
from PyQt6 import uic, QtCore

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    treeView: QTreeView = ui.treeView
    model1 = QStandardItemModel()
    model2 = QFileSystemModel()
    model1.setHorizontalHeaderLabels(["分类", "书名", "作者", "价格"])
    kindP = QStandardItem("Python")
    kindP.appendRow([QStandardItem(""), QStandardItem("Python入门到入土"), QStandardItem("Jack"), QStandardItem("20")])
    model1.appendRow(kindP)

    kindJ = QStandardItem("Java")
    kindJ.appendRow(
        [QStandardItem(""), QStandardItem("Java程序设计基础"), QStandardItem("陈国君"), QStandardItem("99")])
    model1.appendRow(kindJ)

    kindC = QStandardItem("C")
    kindC.appendRow(
        [QStandardItem(""), QStandardItem("C语言发展史"), QStandardItem("亚历山大·奥利贝尔"), QStandardItem("50")])
    model1.appendRow(kindC)

    # model1.appendRow(["Code", "Python入门到入土", "Jack", "20"])
    treeView.setModel(model1)
    treeView.expandAll()
    ui.show()
    sys.exit(app.exec())
