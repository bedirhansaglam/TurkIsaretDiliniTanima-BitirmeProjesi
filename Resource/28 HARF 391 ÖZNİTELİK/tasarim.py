# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tasarim.ui'
#
# Created: Tue Mar 27 14:56:13 2018
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
        Dialog.resize(1236, 754)
        self.groupBox_26 = QtGui.QGroupBox(Dialog)
        self.groupBox_26.setGeometry(QtCore.QRect(10, 20, 1201, 721))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_26.setFont(font)
        self.groupBox_26.setTitle(_fromUtf8(""))
        self.groupBox_26.setObjectName(_fromUtf8("groupBox_26"))
        self.btn_dosyaYukle3 = QtGui.QPushButton(self.groupBox_26)
        self.btn_dosyaYukle3.setGeometry(QtCore.QRect(1040, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_dosyaYukle3.setFont(font)
        self.btn_dosyaYukle3.setObjectName(_fromUtf8("btn_dosyaYukle3"))
        self.label_4 = QtGui.QLabel(self.groupBox_26)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.table_all_data = QtGui.QTableWidget(self.groupBox_26)
        self.table_all_data.setGeometry(QtCore.QRect(10, 50, 1181, 361))
        self.table_all_data.setObjectName(_fromUtf8("table_all_data"))
        self.table_all_data.setColumnCount(0)
        self.table_all_data.setRowCount(0)
        self.gb_classification = QtGui.QGroupBox(self.groupBox_26)
        self.gb_classification.setGeometry(QtCore.QRect(10, 420, 481, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gb_classification.setFont(font)
        self.gb_classification.setObjectName(_fromUtf8("gb_classification"))
        self.cb_classificier = QtGui.QComboBox(self.gb_classification)
        self.cb_classificier.setGeometry(QtCore.QRect(10, 40, 421, 41))
        self.cb_classificier.setObjectName(_fromUtf8("cb_classificier"))
        self.cb_classificier.addItem(_fromUtf8(""))
        self.cb_classificier.addItem(_fromUtf8(""))
        self.cb_classificier.addItem(_fromUtf8(""))
        self.cb_classificier.addItem(_fromUtf8(""))
        self.cb_classificier.addItem(_fromUtf8(""))
        self.btn_split = QtGui.QPushButton(self.gb_classification)
        self.btn_split.setGeometry(QtCore.QRect(270, 180, 191, 51))
        self.btn_split.setObjectName(_fromUtf8("btn_split"))
        self.label = QtGui.QLabel(self.gb_classification)
        self.label.setGeometry(QtCore.QRect(20, 110, 171, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.hs_test_value = QtGui.QSlider(self.gb_classification)
        self.hs_test_value.setGeometry(QtCore.QRect(200, 120, 160, 22))
        self.hs_test_value.setOrientation(QtCore.Qt.Horizontal)
        self.hs_test_value.setObjectName(_fromUtf8("hs_test_value"))
        self.lbl_hs_value = QtGui.QLabel(self.gb_classification)
        self.lbl_hs_value.setGeometry(QtCore.QRect(380, 100, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_hs_value.setFont(font)
        self.lbl_hs_value.setObjectName(_fromUtf8("lbl_hs_value"))
        self.gb_menu = QtGui.QGroupBox(self.groupBox_26)
        self.gb_menu.setGeometry(QtCore.QRect(510, 420, 681, 271))
        self.gb_menu.setObjectName(_fromUtf8("gb_menu"))
        self.btn_confusion = QtGui.QPushButton(self.gb_menu)
        self.btn_confusion.setGeometry(QtCore.QRect(20, 200, 250, 60))
        self.btn_confusion.setObjectName(_fromUtf8("btn_confusion"))
        self.pb_x_test = QtGui.QPushButton(self.gb_menu)
        self.pb_x_test.setGeometry(QtCore.QRect(300, 50, 250, 60))
        self.pb_x_test.setObjectName(_fromUtf8("pb_x_test"))
        self.pb_x_train = QtGui.QPushButton(self.gb_menu)
        self.pb_x_train.setGeometry(QtCore.QRect(20, 50, 250, 60))
        self.pb_x_train.setObjectName(_fromUtf8("pb_x_train"))
        self.pb_y_test = QtGui.QPushButton(self.gb_menu)
        self.pb_y_test.setGeometry(QtCore.QRect(300, 120, 250, 60))
        self.pb_y_test.setObjectName(_fromUtf8("pb_y_test"))
        self.pb_y_train = QtGui.QPushButton(self.gb_menu)
        self.pb_y_train.setGeometry(QtCore.QRect(20, 120, 250, 60))
        self.pb_y_train.setObjectName(_fromUtf8("pb_y_train"))
        self.lbl_basari = QtGui.QLabel(self.gb_menu)
        self.lbl_basari.setGeometry(QtCore.QRect(310, 220, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_basari.setFont(font)
        self.lbl_basari.setObjectName(_fromUtf8("lbl_basari"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Turkish Sign Language Offline Test -", None))
        self.btn_dosyaYukle3.setText(_translate("Dialog", "Verileri Yükle", None))
        self.label_4.setText(_translate("Dialog", "Bütün Veriler :", None))
        self.gb_classification.setTitle(_translate("Dialog", "Sınıflandırıcı Seç", None))
        self.cb_classificier.setItemText(0, _translate("Dialog", "Random Forest", None))
        self.cb_classificier.setItemText(1, _translate("Dialog", "Neural Network", None))
        self.cb_classificier.setItemText(2, _translate("Dialog", "Gausian Navie Bayes", None))
        self.cb_classificier.setItemText(3, _translate("Dialog", "Support Vector Machine", None))
        self.cb_classificier.setItemText(4, _translate("Dialog", "Decision Tree", None))
        self.btn_split.setText(_translate("Dialog", "Train & Test", None))
        self.label.setText(_translate("Dialog", "Test Verisi Yüzdesi :", None))
        self.lbl_hs_value.setText(_translate("Dialog", "% 0", None))
        self.gb_menu.setTitle(_translate("Dialog", "Menu", None))
        self.btn_confusion.setText(_translate("Dialog", "Confusion Matrix", None))
        self.pb_x_test.setText(_translate("Dialog", "X Test", None))
        self.pb_x_train.setText(_translate("Dialog", "X Train", None))
        self.pb_y_test.setText(_translate("Dialog", "Y Test", None))
        self.pb_y_train.setText(_translate("Dialog", "Y Train", None))
        self.lbl_basari.setText(_translate("Dialog", "Başarı Değeri : ", None))

