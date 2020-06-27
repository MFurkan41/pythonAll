# By Muhammed Furkan YOLAL
# By Muhammed Furkan YOLAL
# By Muhammed Furkan YOLAL

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sqlite3
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import requests
import shutil


sys.setrecursionlimit(3000)


def validate_email(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return True
    return False


def SifreSor(k_adi, sifre, mail):
    mesaj = MIMEMultipart('alternative')
    mesaj["From"] = "noreply24356@gmail.com"
    mesaj["To"] = mail
    mesaj["Subject"] = "Şifremi Unuttum"
    html = """
    <p></p>
    <div class="m_-5463809295285811295sm_no_padding">
    <table border="0" cellpadding="0" cellspacing="0" style="width: 519px;">
    <tbody>
    <tr>
    <td style="width: 515px;">
    <table border="0" cellpadding="0" cellspacing="0" width="300" height="300" style="width: 4529px;">
    <tbody>
    <tr>
    <td style="width: 4525px;"><img src="http://python.furkanyolal.com.tr/wp-content/uploads/2018/12/unnamed.png" alt="password ile ilgili g&Atilde;&para;rsel sonucu" width="485" height="323" /><br />
    <h1>Merhaba Şifrenimi Unutmuştun!</h1>
    <p>Şifreni isteğin &uuml;zerine sana bu maili g&ouml;nderdik!</p>
    <div>
    <table border="0" cellpadding="0" cellspacing="0" style="width: 460px;">
    <tbody>
    <tr>
    <td align="center" style="width: 456px;">
    <div></div>
    <h3>Merhaba Sayın {};</h3>
    <h4>Mail: {}</h4>
    <h4>Şifre: {}</h4>
    </td>
    </tr>
    </tbody>
    </table>
    <img src="http://python.furkanyolal.com.tr/wp-content/uploads/2018/12/locker_53876-25496.jpg" width="216" height="144" /></div>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </div>
    """.format(k_adi, mail, sifre)
    mesaj_govdesi = MIMEText(html, "html")
    mesaj.attach(mesaj_govdesi)
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("noreply24356@gmail.com", "NoReply24356*")
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    mail.close()


class LoginPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.baglanti_olustur()

    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()

        self.cursor.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT, email TEXT)")
        baglanti.commit()

    def init_ui(self):

        self.eposta_yazi = QtWidgets.QLabel("E-Posta :")
        self.parola_yazi = QtWidgets.QLabel("Parola :        ")
        self.eposta = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.kaydol = QtWidgets.QPushButton("Kayıt Ol")
        self.sifremi_unuttum = QtWidgets.QPushButton("Şifremi Unuttum?")
        self.yazi_alani = QtWidgets.QLabel("")

        h_box1 = QtWidgets.QHBoxLayout()
        h_box2 = QtWidgets.QHBoxLayout()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)

        h_box1.addStretch()
        h_box1.addWidget(self.eposta_yazi)
        h_box1.addWidget(self.eposta)
        h_box1.addStretch()

        h_box2.addStretch()
        h_box2.addWidget(self.parola_yazi)
        h_box2.addWidget(self.parola)
        h_box2.addStretch()

        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.giris)
        v_box.addWidget(self.kaydol)
        v_box.addWidget(self.sifremi_unuttum)

        self.setLayout(v_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)
        self.kaydol.clicked.connect(self.register)
        self.sifremi_unuttum.clicked.connect(self.sifre)
        self.setWindowIcon(QtGui.QIcon('new_icon.png'))
        self.setGeometry(550, 250, 250, 150)
        self.rp = RegisterPage()
        self.su = Sifremi_Unuttum()
        self.gb = GirisBasarili()
        self.show()

    def login(self):
        eposta = self.eposta.text()
        par = self.parola.text()

        self.cursor.execute("Select * from üyeler where email = ? and parola = ?", (eposta, par))
        self.data = self.cursor.fetchall()
        if len(self.data) == 0:
            self.yazi_alani.setText("Giriş Başarısız")
        else:
            self.gb.show()
            self.eposta.setText("")
            self.parola.setText("")
            self.hide()

    def register(self):
        self.rp.show()
        self.yazi_alani.setText("Başarıyla Kaydoldun!")
        self.eposta.setText("")
        self.parola.setText("")
        self.hide()

    def sifre(self):
        self.su.show()
        self.yazi_alani.setText("Şifren E-Posta Hesabına Gönderildi!")
        self.eposta.setText("")
        self.parola.setText("")
        self.hide()


# Register Sekmesi
class RegisterPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("database.db")
        self.cursor = self.baglanti.cursor()

        self.baglanti.commit()

    def init_ui(self):
        self.k_adi_yazi = QtWidgets.QLabel("Kullanıcı Adı :")
        self.parola_yazi = QtWidgets.QLabel("Parola :        ")
        self.eposta_yazi = QtWidgets.QLabel("E-Posta :      ")
        self.k_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.eposta = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.kaydol = QtWidgets.QPushButton("Kayıt Ol")
        self.geri = QtWidgets.QPushButton("<---- Geri")
        self.yazi_alani = QtWidgets.QLabel("")

        h_box1 = QtWidgets.QHBoxLayout()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box3 = QtWidgets.QHBoxLayout()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)

        h_box1.addStretch()
        h_box1.addWidget(self.k_adi_yazi)
        h_box1.addWidget(self.k_adi)
        h_box1.addStretch()

        h_box2.addStretch()
        h_box2.addWidget(self.parola_yazi)
        h_box2.addWidget(self.parola)
        h_box2.addStretch()

        h_box3.addStretch()
        h_box3.addWidget(self.eposta_yazi)
        h_box3.addWidget(self.eposta)
        h_box3.addStretch()

        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.kaydol)
        v_box.addWidget(self.geri)

        self.setLayout(v_box)

        self.kaydol.clicked.connect(self.register1)
        self.geri.clicked.connect(self.geri_git)
        self.setGeometry(550, 250, 250, 150)
        self.setWindowIcon(QtGui.QIcon('new_icon.png'))
        self.setWindowTitle("Kayıt Ol")

    def register1(self):
        ad = self.k_adi.text()
        parola = self.parola.text()
        eposta = self.eposta.text()
        if len(ad) == 0 or len(parola) == 0:
            self.yazi_alani.setText("Lütfen Alanları Doldurunuz.")
        else:
            if (validate_email(str(eposta)) == True):
                self.cursor.execute("INSERT INTO üyeler (kullanıcı_adı, parola, email) VALUES (?,?,?)",(ad, parola, eposta))
                self.baglanti.commit()
                time.sleep(1)
                loginpencere.show()
                self.hide()
            else:
                self.yazi_alani.setText("Lütfen Geçerli Bir E-Posta Adresi Giriniz.")

    def geri_git(self):
        self.hide()
        loginpencere.show()
        loginpencere.yazi_alani.setText("")


class Sifremi_Unuttum(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("database.db")
        self.cursor = self.baglanti.cursor()
        self.baglanti.commit()

    def init_ui(self):
        self.email_yazi = QtWidgets.QLabel("E-Posta :")
        self.kul_yazi = QtWidgets.QLabel("Kullanıcı Adı :")
        self.email = QtWidgets.QLineEdit()
        self.kul_adi = QtWidgets.QLineEdit()
        self.gonder = QtWidgets.QPushButton("Şifremi Gönder")
        self.geri = QtWidgets.QPushButton("<---- Geri")
        self.yazi_alani = QtWidgets.QLabel("")

        self.v_box1 = QtWidgets.QVBoxLayout()
        self.h_box1 = QtWidgets.QHBoxLayout()
        self.h_box2 = QtWidgets.QHBoxLayout()

        self.v_box1.addLayout(self.h_box2)
        self.v_box1.addLayout(self.h_box1)

        self.h_box1.addWidget(self.email_yazi)
        self.h_box1.addWidget(self.email)

        self.h_box2.addWidget(self.kul_yazi)
        self.h_box2.addWidget(self.kul_adi)

        self.v_box1.addWidget(self.yazi_alani)
        self.v_box1.addWidget(self.gonder)
        self.v_box1.addWidget(self.geri)

        self.gonder.clicked.connect(self.click1)
        self.geri.clicked.connect(self.geri_git)
        self.setWindowTitle("Şifremi Unuttum")
        self.setGeometry(550, 250, 250, 150)
        self.setWindowIcon(QtGui.QIcon('new_icon.png'))
        self.setLayout(self.v_box1)
        
    def click1(self):
        email = str(self.email.text())
        kul_adi = str(self.kul_adi.text())
        self.cursor.execute("Select * from üyeler where email = ? and kullanıcı_adı = ?", (email, kul_adi))
        self.data = self.cursor.fetchall()
        if len(self.data) == 0:
            self.yazi_alani.setText("Böyle bir hesap bulunamadı.")
        else:
            data = self.data[0]
            SifreSor(data[0], data[1], data[2])
            self.kul_adi.setText("")
            self.email.setText("")
            self.hide()
            loginpencere.show()

    def geri_git(self):
        self.hide()
        loginpencere.show()
        loginpencere.yazi_alani.setText("")


class GirisBasarili(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.hosgeldiniz = QtWidgets.QLabel("Hoşgeldiniz")
        self.cikis = QtWidgets.QPushButton("Çıkış Yap")

        v_box1 = QtWidgets.QVBoxLayout()
        v_box1.addWidget(self.hosgeldiniz)
        v_box1.addWidget(self.cikis)

        self.setLayout(v_box1)
        self.cikis.clicked.connect(self.cikis_yap)
        self.setWindowTitle("Giriş Yaptın!")
        self.setWindowIcon(QtGui.QIcon('new_icon.png'))
        self.setGeometry(550, 300, 250, 50)
        self.hide()

    def cikis_yap(self):
        loginpencere.show()
        loginpencere.yazi_alani.setText("")
        self.hide()


app = QtWidgets.QApplication(sys.argv)

loginpencere = LoginPage()
#sys.exit(app.exec_())
sys.exit(app.exec_())

# By Muhammed Furkan YOLAL
# By Muhammed Furkan YOLAL
# By Muhammed Furkan YOLAL
