# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confusion.ui'
#
# Created: Tue Mar 27 11:26:47 2018
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
        Dialog.resize(1366, 789)
        self.table_confusion_matrix = QtGui.QTableWidget(Dialog)
        self.table_confusion_matrix.setGeometry(QtCore.QRect(10, 40, 1350, 731))
        self.table_confusion_matrix.setObjectName(_fromUtf8("table_confusion_matrix"))
        self.table_confusion_matrix.setColumnCount(0)
        self.table_confusion_matrix.setRowCount(0)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Karmaşıklık Matrisi", None))
        self.label_5.setText(_translate("Dialog", "Confusion Matrix", None))

