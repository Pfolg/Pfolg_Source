# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME Hello_world
AUTHOR Pfolg
TIME 2025/2/26 18:27
"""
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

app = QApplication(sys.argv)  # 创建一个应用
print(sys.argv)
# print(app.arguments())
window = QWidget()
window.setWindowTitle("App")
window.resize(400, 300)  # 宽高
window.move(400, 200)
window.show()

label = QLabel()
label.setParent(window)
label.setText("Hello")
label.resize(150, 60)
label.setStyleSheet("background-color:#367ed9;padding:10px")
label.move(20, 20)
label.show()
sys.exit(app.exec())  # 开始执行程序，并且进入消息循环等待
