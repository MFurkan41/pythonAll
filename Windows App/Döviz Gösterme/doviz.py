# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import requests

url = "http://data.fixer.io/api/latest?access_key=74ef373e877920888f67325ed6d4e566"
response = requests.get(url)
data = response.json()
doviz_listesi = list(data["rates"].keys())

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 188)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(40, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 80, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.qlineedit = QtWidgets.QLineEdit(Form)
        self.qlineedit.setText("0")
        self.qlineedit.setGeometry(QtCore.QRect(40, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.qlineedit.setFont(font)
        self.qlineedit.setObjectName("qlineedit")
        self.qlineedit_2 = QtWidgets.QLineEdit(Form)
        self.qlineedit_2.setGeometry(QtCore.QRect(280, 70, 161, 31))
        self.qlineedit_2.setText("0")
        self.qlineedit_2.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.qlineedit_2.setFont(font)
        self.qlineedit_2.setObjectName("qlineedit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Döviz Çevirme Programı"))
        self.comboBox_2.addItems(doviz_listesi)
        self.comboBox.addItems(doviz_listesi)
        self.pushButton.setText(_translate("Form", "Döviz Çevir"))
        self.label.setText(_translate("Form", "----->"))
    def on_click(self):
        firstCurrency = self.comboBox.currentText()
        secondCurrency = self.comboBox_2.currentText()
        firstAmount = self.qlineedit.text()
        secondAmount = self.qlineedit_2.text()
        result = ((float(data["rates"][secondCurrency]) / float(data["rates"][firstCurrency]))*float(firstAmount))
        result = round(result, 4)
        self.qlineedit_2.setText(str(result))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

# By Muhammed Furkan YOLAL
