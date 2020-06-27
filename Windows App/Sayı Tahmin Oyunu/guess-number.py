from PyQt5 import QtWidgets
import sys
from random import randint

class SayiTahmin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        #Bu değerleri değiştirebilirsin..
        self.d_can = 4
        self.den = 1
        self.e = 10

        self.liste = []
        for i in range(2,self.d_can+1):
            self.liste.append(i)
        self.sayi = randint(self.den, self.e)
        self.can = self.d_can
        self.baslik = QtWidgets.QLabel("Sayı Tahmin Oyunu")
        self.yazi = QtWidgets.QLabel("{}'den {}'a kadar bir sayı giriniz.".format(self.den,self.e))
        self.bilgi = QtWidgets.QLabel("")
        self.bilgi.hide()
        self.can_alani = QtWidgets.QLabel("")
        self.can_alani.setText("Can: {}".format(self.can))
        self.yazi_alani = QtWidgets.QLineEdit()
        self.gonder = QtWidgets.QPushButton("Dene")
        self.sifirla = QtWidgets.QPushButton("Yeniden Başlat")

        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addWidget(self.yazi_alani)
        self.h_box.addWidget(self.gonder)
        self.h_box.addWidget(self.sifirla)

        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addWidget(self.baslik)
        self.v_box.addWidget(self.yazi)
        self.v_box.addWidget(self.bilgi)
        self.v_box.addWidget(self.can_alani)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.gonder.clicked.connect(self.buton)
        self.sifirla.clicked.connect(self.buton)
        self.setWindowTitle("Sayı Tahmin Oyunu")
        self.setGeometry(550,300,350,100)
        self.show()
    def buton(self):
        sender = self.sender()
        if (sender.text() == "Dene"):
            if (self.can in self.liste):
                self.bilgi.show()
                if(len(self.yazi_alani.text()) <= 0):
                    self.bilgi.setText("Lütfen Bir Değer Giriniz.")
                else:
                    self.bilgi.show()
                    self.deger = int(self.yazi_alani.text())
                    if(self.deger == self.sayi):
                        self.bilgi.setText("Sayıyıyı Bildin! Sayı: {}".format(self.sayi))
                    elif(self.deger > self.sayi):
                        self.bilgi.setText("Malesef Bilemedin.. Daha Küçük Bir Sayı Girmelisin..")
                        self.can = self.can - 1
                        self.can_alani.setText("Can: {}".format(self.can))
                    elif(self.deger > self.e or self.deger < self.den):
                        self.bilgi.setText("Lütfen belirlenen aralıklar arasında bir değer gir.")
                        self.can_alani.setText("Can: {}".format(self.can))
                    else:
                        self.bilgi.setText("Malesef Bilemedin.. Daha Büyük Bir Sayı Girmelisin..")
                        self.can = self.can - 1
                        self.can_alani.setText("Can: {}".format(self.can))
            else:
                if (self.deger == self.sayi):
                    self.bilgi.setText("Sayıyıyı Bildin! Sayı: {}".format(self.sayi))
                else:
                    self.bilgi.setText("Canın Bitti. Tekrar Başla! Sayı: {}".format(self.sayi))
                    self.can_alani.setText("Can: {}".format(0))
        else:
            self.can = self.d_can
            self.can_alani.setText("Can: {}".format(self.can))
            self.sayi = randint(self.den, self.e)
            self.bilgi.hide()
            self.yazi_alani.clear()

app = QtWidgets.QApplication(sys.argv)

isim = SayiTahmin()

sys.exit(app.exec_())
