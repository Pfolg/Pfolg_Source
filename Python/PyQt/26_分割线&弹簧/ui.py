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
        Form.resize(597, 521)
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setGeometry(QtCore.QRect(20, 10, 351, 131))
        self.line.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=Form)
        self.line_2.setGeometry(QtCore.QRect(20, 80, 171, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 54, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 54, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(260, 20, 54, 16))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 170, 111, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Users/21460/Pictures/fontawesome-free-6.7.2-desktop/svgs/solid/futbol.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.dial = QtWidgets.QDial(parent=Form)
        self.dial.setGeometry(QtCore.QRect(240, 370, 50, 64))
        self.dial.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.horizontalScrollBar = QtWidgets.QScrollBar(parent=Form)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(300, 190, 160, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalScrollBar = QtWidgets.QScrollBar(parent=Form)
        self.verticalScrollBar.setGeometry(QtCore.QRect(490, 190, 16, 160))
        self.verticalScrollBar.setProperty("value", 50)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setInvertedAppearance(False)
        self.verticalScrollBar.setInvertedControls(True)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_5.setText(_translate("Form", "设置"))
