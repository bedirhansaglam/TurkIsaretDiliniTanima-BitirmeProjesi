# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'x_test.ui'
#
# Created: Tue Mar 27 14:47:50 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1366, 762)
        self.table_x_test = QtGui.QTableWidget(Dialog)
        self.table_x_test.setGeometry(QtCore.QRect(10, 10, 1350, 750))
        self.table_x_test.setObjectName(_fromUtf8("table_x_test"))
        self.table_x_test.setColumnCount(0)
        self.table_x_test.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "X TEST", None))

