# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(471, 311)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 40, 271, 21))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 121, 21))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(170, 70, 271, 21))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 121, 21))
        self.label_3.setObjectName("label_3")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(170, 100, 271, 21))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 121, 21))
        self.label_4.setObjectName("label_4")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(170, 130, 271, 21))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 121, 21))
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(170, 160, 271, 21))
        self.dateEdit.setObjectName("dateEdit")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(170, 190, 271, 21))
        self.spinBox.setObjectName("spinBox")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 121, 21))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Model Path:"))
        self.label_2.setText(_translate("Dialog", "Trade Path:"))
        self.label_3.setText(_translate("Dialog", "Model Name:"))
        self.label_4.setText(_translate("Dialog", "Reference Credit:"))
        self.label_5.setText(_translate("Dialog", "Model Date:"))
        self.label_6.setText(_translate("Dialog", "Shock Size:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())