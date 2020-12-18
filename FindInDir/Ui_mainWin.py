# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(814, 526)
        self.listMessage = QtWidgets.QListWidget(Dialog)
        self.listMessage.setGeometry(QtCore.QRect(0, 0, 711, 361))
        self.listMessage.setObjectName("listMessage")
        self.container = QtWidgets.QWidget(Dialog)
        self.container.setGeometry(QtCore.QRect(0, 360, 711, 111))
        self.container.setObjectName("container")
        self.labelStatus = QtWidgets.QLabel(self.container)
        self.labelStatus.setGeometry(QtCore.QRect(10, 60, 701, 31))
        self.labelStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelStatus.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelStatus.setText("")
        self.labelStatus.setObjectName("labelStatus")
        self.lineEdit = QtWidgets.QLineEdit(self.container)
        self.lineEdit.setGeometry(QtCore.QRect(8, 8, 381, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.btnSearchText = QtWidgets.QPushButton(self.container)
        self.btnSearchText.setGeometry(QtCore.QRect(400, 30, 131, 32))
        self.btnSearchText.setObjectName("btnSearchText")
        self.btnSearchPlist = QtWidgets.QPushButton(self.container)
        self.btnSearchPlist.setGeometry(QtCore.QRect(550, 30, 111, 32))
        self.btnSearchPlist.setObjectName("btnSearchPlist")
        self.label_2 = QtWidgets.QLabel(self.container)
        self.label_2.setGeometry(QtCore.QRect(440, 10, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.container)
        self.label_3.setGeometry(QtCore.QRect(590, 10, 41, 16))
        self.label_3.setObjectName("label_3")
        self.splitter = QtWidgets.QSplitter(self.container)
        self.splitter.setGeometry(QtCore.QRect(8, 30, 381, 32))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.comboDir = QtWidgets.QComboBox(self.splitter)
        self.comboDir.setEditable(True)
        self.comboDir.setObjectName("comboDir")
        self.comboDir.addItem("")
        self.comboDir.addItem("")

        self.retranslateUi(Dialog)
        self.btnSearchText.clicked.connect(Dialog.doFindText)
        self.btnSearchPlist.clicked.connect(Dialog.doFindPlist)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Serch Directory"))
        self.lineEdit.setText(_translate("Dialog", "avformat_find_stream_info"))
        self.btnSearchText.setText(_translate("Dialog", "Search -R text"))
        self.btnSearchPlist.setText(_translate("Dialog", "Search plist"))
        self.label_2.setText(_translate("Dialog", "*.cc   *.h"))
        self.label_3.setText(_translate("Dialog", ".plist"))
        self.label.setText(_translate("Dialog", "In Dir :     home   /"))
        self.comboDir.setItemText(0, _translate("Dialog", "electron11/src"))
        self.comboDir.setItemText(1, _translate("Dialog", "Preferences"))
