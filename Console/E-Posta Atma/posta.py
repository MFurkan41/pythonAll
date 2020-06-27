import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
"""
SMTP Modülü ile mail gönderme

İlk olarak daha az güvenli uygulamalar için öncelikle aşağıdaki linke gidiyoruz ve güvenliği
kaldırıyoruz.

https://myaccount.google.com/lesssecureapps

"""

mesaj = MIMEMultipart()  # Mail yapımızı oluşturuyoruz.

mesaj["From"] =  "fyolal2006@gmail.com" # Kimden Göndereceğimiz

mesaj["To"] = "fyolal2006@gmail.com" # Kime Göndereceğimiz

mesaj["Subject"] = "Smtp Mail Gönderme"  # Mailimizin Konusu


# Mailimizin İçeriği
yazi = """

Merhaba, Python ile mail gönderiyorum.    

Muhammed Furkan YOLAL


"""


mesaj_govdesi =  MIMEText(yazi,"plain")  # Mailimizin gövdesini bu sınıftan oluşturuyoruz.

mesaj.attach(mesaj_govdesi) # Mailimizin gövdesini mail yapımıza ekliyoruz.



try:
    mail =  smtplib.SMTP("smtp.gmail.com",587)  # SMTP objemizi oluşturuyoruz ve gmail smtp server'ına bağlanıyoruz.

    mail.ehlo() # SMTP serverına kendimizi tanıtıyoruz.

    mail.starttls() # Adresimizin ve Parolamızın şifrelenmesi için gerekli

    mail.login("fyolal2006@gmail.com","**") # SMTP server'ına giriş yapıyoruz. Kendi mail adresimizi ve parolamızı yapıyoruz.

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())  # Mailimizi gönderiyoruz.
    print("Mail başarıyla gönderildi....")
    mail.close()  # Smtp serverımızın bağlantısını koparıyoz.

except:
    sys.stderr.write("Mail göndermesi başarısız oldu...") # Herhangi bir bağlanma sorunu veya mail gönderme sorunu olursa
    sys.stderr.flush()
