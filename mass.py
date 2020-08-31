# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mass.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt

class Ui_Form(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(653, 214)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 180, 591, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.button = QtWidgets.QPushButton("Получить", self)
        # button.move(50,50)
        self.button.setGeometry(QtCore.QRect(470, 2, 120, 25))

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 301, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(340, 10, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(622, 10, 20, 16))
        self.label_6.setObjectName("label_6")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(12, 188, 481, 15))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(330, 30, 285, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(620, 30, 20, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 631, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 120, 171, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 145, 171, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 171, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 145, 171, 20))
        self.label_5.setObjectName("label_5")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(330, 56, 171, 21))
        self.checkBox.setObjectName("checkBox")

        self.comboBox_1 = QtWidgets.QComboBox(Dialog)
        self.comboBox_1.setGeometry(QtCore.QRect(330, 30, 285, 20))
        self.comboBox_1.setObjectName("comboBox")
        self.comboBox_1.setVisible(False)

        self.retranslateUi(Dialog)
        #self.buttonBox.accepted.connect(Dialog.accept)
        #self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "Добавление навыков"))
        self.comboBox.setItemText(1, _translate("Dialog", "Удаление навыков"))
        self.comboBox.setItemText(2, _translate("Dialog", "Смена профиля (только из Default)"))
        self.comboBox.setItemText(3, _translate("Dialog", "Назначение СВ"))
        self.label.setText(_translate("Dialog", "Действие"))
        self.label_2.setText(_translate("Dialog", "Название скила"))
        self.label_3.setText(_translate("Dialog", "Ссылка на отдел"))
        self.label_4.setText(_translate("Dialog", "Логин"))
        self.label_5.setText(_translate("Dialog", "Пароль"))
        self.label_6.setText(_translate("Dialog", "Ур."))
        self.checkBox.setText(_translate("Dialog", "Оставить Firefox открытым"))
        self.lineEdit_3.setText(_translate("Dialog", "msv_adm"))
        self.lineEdit_4.setText(_translate("Dialog", "1234"))

