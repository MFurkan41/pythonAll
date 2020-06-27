# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QApplication, QWidget ,QMessageBox)
import sys
import win32clipboard
from time import sleep as bekle

class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        msg = QMessageBox()
        msg.setWindowTitle("K-Sayacı")
        msg.setIcon(QMessageBox.Information)
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        msg.setText("Karakter Uzunluğu ( ):  " + str(len(data)) + "\nKarakter Uzunluğu ():  "+ str(len(data.replace(" ",""))))
        msg.exec_()
        sys.exit()
        
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    sys.exit(app.exec_())
