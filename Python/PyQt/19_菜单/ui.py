# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_File = QtGui.QAction(parent=MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.action = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Users/21460/Pictures/fontawesome-free-6.7.2-desktop/svgs/regular/file.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action.setIcon(icon)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Users/21460/Pictures/fontawesome-free-6.7.2-desktop/svgs/regular/folder.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_2.setIcon(icon1)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../Users/21460/Pictures/fontawesome-free-6.7.2-desktop/svgs/regular/floppy-disk.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_3.setIcon(icon2)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setIcon(icon2)
        self.action_4.setObjectName("action_4")
        self.menuFile.addAction(self.action_2)
        self.menuFile.addAction(self.action)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_3)
        self.menuFile.addAction(self.action_4)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.action.setText(_translate("MainWindow", "打开文件"))
        self.action_2.setText(_translate("MainWindow", "打开文件夹"))
        self.action_3.setText(_translate("MainWindow", "保存"))
        self.action_3.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_4.setText(_translate("MainWindow", "另存为"))
