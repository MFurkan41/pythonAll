import time
import sqlite3
from itertools import chain
y = False
x = False
d = 1
id = 0
u_id = 0
root_user = "root"
root_pass = "1234"
con = sqlite3.connect("allusers.db")
cursor = con.cursor()
id +=1
try:
    cursor.execute("INSERT INTO accounts ( id , username , password) VALUES ( ? , ? , ?)", ( id , (root_user) , (root_pass)))
except sqlite3.OperationalError:
        cursor.execute("CREATE TABLE accounts (id INT , username TEXT, password TEXT)")
accounts_username = []
accounts_password = []
def hesapolusturu():
    username = input("Lütfen Kullanıcı Adınız Giriniz: \n")
    return username
def hesapolusturp():
    password = input("Lütfen Şifrenizi Giriniz: \n")
    return password
while (d==1):
    try:
        cursor.execute("SELECT * FROM accounts")
        allacc = cursor.fetchall()
    except sqlite3.OperationalError:
        cursor.execute("CREATE TABLE accounts (id INT , username TEXT, password TEXT)")
    cursor.execute("SELECT Count (*) FROM accounts")
    recordcount = cursor.fetchone()
    cursor.execute("SELECT id FROM accounts ORDER BY id DESC")
    lastid = cursor.fetchone()
    i = 1

    sayi = (input("1- Giriş Yap\n2- Kayıt Ol\n3- Sistemden Çık\nİşleminiz: "))
    if sayi.isdigit():
        if (int(sayi) == 1) or (int(sayi) == 2) or (int(sayi) == 3):
            if int(sayi) == 1:
                if (recordcount[0]) < 1:
                    print("Kayıtlı hiçbir hesap yoktur. Lütfen kaydolunuz.")
                else :
                    u1 = str(input("Lütfen Kullanıcı Adınız Giriniz: \n"))
                    p1 = str(input("Lütfen Şifrenizi Giriniz: \n"))
                    z = 0
                    if z <= recordcount[0]:
                        if (root_user) == u1 and (root_pass) == p1:
                            try:
                                u_id = 1
                                print("(Root)Başarıyla Giriş Yaptın.")
                                x = True
                                z+=1
                                cursor.execute("SELECT id FROM accounts WHERE ( ? )", (root_user ,))
                                u_id = cursor.fetchone()
                            except IndexError:
                                print("Sistemde bir hata oluştu.")
                        elif (u1) in chain(*allacc) and (str(p1)) in chain(*allacc):
                            try:
                                cursor.execute("SELECT id FROM accounts WHERE ( ? )", (u1 ,))
                                u_id = cursor.fetchone()

                                print("Başarıyla Giriş Yaptın.")
                                y = True
                                z+=1
                            except IndexError:
                                print("Sistemde bir hata oluştu.")
                        else:
                            try:
                                print("Kullanıcı Adınız veya Şifreniz Yanlıştır.")
                                z+=1
                            except IndexError:
                                print("Sistemde bir hata oluştu.")
                    if (x == True):
                        d = d - 1
                        r_option = int(input("1- Hesapları Listele \n2- Hesap Sil \n3- Çıkış Yap \n4- Root Şifresini Değiştir \n5- Root Kullanıcı Adını Değiştir\n İşleminiz: "))
                        if r_option == 1:
                            try:
                                if recordcount[0] < 1:
                                    print("Kayıtlı hiçbir hesap yoktur.")
                                else:
                                    for y in range(lastid[0]):
                                        print((allacc)[y])
                                        y += 1
                                    print("Hesaplar Listelendi.")
                            except IndexError:
                                print("Hesaplar Listelendi.")
                        elif r_option == 2:
                            y = 1
                            try:
                                for y in range(lastid[0]):
                                    y += 1
                            except IndexError:
                                print()
                            if (lastid[0]) < 1:
                                print("Kayıtlı hiçbir hesap yoktur.")

                            else:
                                kindex= int(input("Kaç numaralı hesabı silmek istiyorsun?\n"))

                                if lastid[0] < kindex:
                                    print(kindex , ". hesap yoktur. Lütfen başka bir hesap giriniz.")
                                else:
                                    print(type(kindex))
                                    delete = "DELETE FROM accounts WHERE id  = ?"
                                    cursor.execute(delete , (kindex , ))
                                    con.commit()
                        elif r_option == 3:
                            print("Çıkış Yapıldı!")
                            d+=1
                        elif r_option == 4:
                            old_pass = str(input("Eski Şifrenizi Giriniz :"))
                            if old_pass == root_pass:
                                new_pass = str(input("Yeni Şifrenizi Giriniz :"))
                                cursor.execute("UPDATE accounts SET password = (?) WHERE id= (?) ", (new_pass, u_id))
                            else:
                                print("Eski Şifrenizi Yanlış Girdiniz.")
                    if (y == True):
                        r_option = int(input("1- Çıkış Yap\n İşleminiz: "))
                        if r_option == 1:
                            print("Çıkış Yapıldı.")
                            y = False
                        
            elif int(sayi) == 2:
                username = hesapolusturu()
                password = hesapolusturp()
                id +=1
                cursor.execute("INSERT INTO accounts ( id , username , password) VALUES ( ? , ? , ?)", ( id ,username , password))
                con.commit()
                print("Hesabın başarıyla eklendi.")

                print(accounts_username)
            elif int(sayi) == 3:
                d-=1
                print("Sistemden Çıkıldı!")

                
                


        else:
            print("Yanlış bir rakam girdin. Lütfen 1, 2 veya 3 yaz!")
    else:
        print("Yanlış bir karakter girdin. Lütfen 1, 2 veya 3 yaz!")
