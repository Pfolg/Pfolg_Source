# -*- coding: UTF-8 -*-
"""
PROJECT_NAME mines_cleaner
PRODUCT_NAME PyCharm
NAME main
AUTHOR Pfolg
TIME 2025/8/16 22:29
"""
import sys

from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QApplication
import mainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = mainWindow.Root()
    app.setWindowIcon(QIcon("image\\circle-radiation.svg"))
    app.setFont(QFont("Maple Mono NF CN"))
    root.show()
    sys.exit(app.exec())
