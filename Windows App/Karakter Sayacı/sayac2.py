import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget, QHBoxLayout,QMessageBox)
from PyQt5 import QtGui,QtCore
import win32clipboard

class basicRadiobuttonExample(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        font = QtGui.QFont()
        font.setPointSize(10)

        self.rbtn1 = QRadioButton('Boşluklu')
        self.rbtn1.setFont(font)
        
        self.rbtn2 = QRadioButton('Boşluksuz')
        self.rbtn2.setFont(font)
        
        self.label2 = QLabel("")
        self.label3 = QLabel("")
        
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(10)

        self.Say = QPushButton("Say")
        self.Say.setFont(font)

        layouth = QHBoxLayout()
        
        layouth.addWidget(self.rbtn1)
        layouth.addStretch()
        layouth.addWidget(self.rbtn2)

        layoutv = QVBoxLayout()

        layoutv.addLayout(layouth)
        layoutv.addWidget(self.Say)
        
        self.Say.setGeometry(QtCore.QRect(82, 97, 111, 41))
        self.setGeometry(780, 410, 300, 150)
        self.setLayout(layoutv)

        
        self.Say.clicked.connect(lambda : self.click(self.rbtn1.isChecked(),self.rbtn2.isChecked()))
        

        self.setWindowTitle('K-Sayacı')

        self.show()

    def click(self,rbtn1,rbtn2):
        if(rbtn1 == True):
            self.hide()
            msg = QMessageBox()
            msg.setWindowTitle("K-Sayacı")
            msg.setIcon(QMessageBox.Information)
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            msg.setText("Karakter Uzunluğu :  " + str(len(data)))
            msg.exec_()
        else:
            self.hide()
            msg = QMessageBox()
            msg.setWindowTitle("K-Sayacı")
            msg.setIcon(QMessageBox.Information)
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            data = data.replace(" ","")
            msg.setText("Karakter Uzunluğu :  " + str(len(data)))
            msg.exec_()


            
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = basicRadiobuttonExample()
    sys.exit(app.exec_())
