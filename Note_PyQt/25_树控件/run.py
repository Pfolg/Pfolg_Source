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
from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem
import sys
from PyQt6 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    treeWidget: QTreeWidget = ui.treeWidget
    treeWidget.setHeaderLabels(["分类", "书名", "作者", "价格"])

    kind1 = QTreeWidgetItem(treeWidget)
    kind1.setText(0, "Python")
    kind1.setIcon(0, QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\brands\python.svg"))
    kind1_child1 = QTreeWidgetItem(kind1)
    kind1_child1.setText(0, "")
    kind1_child1.setText(1, "1")
    kind1_child1.setText(2, "2")
    kind1_child1.setText(3, "3")
    kind1_child1.setCheckState(1, Qt.CheckState.Unchecked)  # 设置复选框，默认未选择

    kind2 = QTreeWidgetItem(treeWidget)
    kind2.setIcon(0, QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\brands\java.svg"))
    kind2.setText(0, "Java")
    kind2_child1 = QTreeWidgetItem(kind2)
    kind2_child1.setText(0, "")
    kind2_child1.setIcon(2, QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\user.svg"))
    kind2_child1.setText(1, "1")
    kind2_child1.setText(2, "2")
    kind2_child1.setText(3, "3")
    kind2_child1.setCheckState(1, Qt.CheckState.Unchecked)

    kind3 = QTreeWidgetItem(treeWidget)
    kind3.setText(0, "C")
    kind3.setIcon(0, QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\regular\file-code.svg"))
    kind3_child1 = QTreeWidgetItem(kind3)
    kind3_child1.setText(0, "")
    kind3_child1.setText(1, "1")
    kind3_child1.setText(2, "2")
    kind3_child1.setText(3, "3")
    kind3_child1.setCheckState(1, Qt.CheckState.Unchecked)

    treeWidget.setAlternatingRowColors(True)  # 设置灰白行间隔 斑马线
    treeWidget.expandAll()
    ui.show()
    sys.exit(app.exec())
