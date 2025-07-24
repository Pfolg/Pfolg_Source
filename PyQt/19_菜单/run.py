# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMenuBar, QMenu, QStyle, QMainWindow
import sys
from PyQt6 import uic


def exitui():
    ui.destroy()
    sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    menubar: QMenuBar = ui.menubar
    menuFile: QMenu = ui.menuFile
    action: QAction = ui.action
    action.setText("Open a file")
    print(action.text())
    menuFile.addSeparator()  # 添加分割线
    # 添加新动作
    actionPrint = QAction()
    actionPrint.setText("Print")
    actionPrint.setIcon(QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\paper-plane.svg"))
    menuFile.addAction(actionPrint)

    menuFile.addAction(QAction(
        QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\share-from-square.svg"), "Share",
        menuFile))
    # 添加新菜单
    testMenu = QMenu(parent=menubar)
    testMenu.setTitle("test")
    menuFile.setToolTip("文件")
    testMenu.setToolTip("test")
    # testMenu.setIcon(QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\lightbulb.svg"))
    menuFile.addMenu(testMenu)
    testMenu.addAction(QAction(
        QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\share-from-square.svg"), "Share",
        testMenu))
    ui.show()
    # ui.destroy()
    exitui()
    sys.exit(app.exec())
