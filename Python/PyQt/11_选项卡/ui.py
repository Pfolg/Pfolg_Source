# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 101, 131))
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 60, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 90, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 30, 101, 131))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setChecked(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(0, 30, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(0, 60, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 90, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Users/21460/Pictures/fontawesome-free-6.7.2-desktop/svgs/regular/moon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(parent=self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.groupBox_2.setTitle(_translate("Form", "GroupBox"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.radioButton_2.setText(_translate("Form", "RadioButton"))
        self.radioButton_3.setText(_translate("Form", "RadioButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("Form", "标签1"))
        self.label.setText(_translate("Form", "This is tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
