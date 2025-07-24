# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMenuBar, QMenu, QStyle, QMainWindow, QToolBar
import sys
from PyQt6 import uic, QtCore


def exitui():
    ui.destroy()
    sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    toolBar: QToolBar = ui.toolBar
    toolBar.addActions([
        QAction(QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\face-grin.svg"), "Smile",
                toolBar),
        QAction(
            QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\face-grin-tongue-squint.svg"),
            "Funny", toolBar)
    ])
    toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
    toolBar.addAction(
        QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\face-surprise.svg"),
        "Surprise")
    # exitui()
    ui.show()
    
    sys.exit(app.exec())
