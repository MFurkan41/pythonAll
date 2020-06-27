
def hesapolustur():
    username = input("Lütfen Kullanıcı Adınız Giriniz: \n")
    password = input("Lütfen Şifrenizi Giriniz: \n")
    return username,password
def girisyap(username,password):
    if any(username in s for s in hesaplar):
        if any(password in s for s in hesaplar):
            print("Başarıyla Giriş Yaptın.")
    else:
        print("Kullanıcı adınız veya şifreniz yanlıştır.")

hesaplar = []
while (True):
    sayi = (input("1- Giriş Yap\n2- Kayıt Ol\n3- Hesap Sil\n4- Hesapları Listele\n"))


    if sayi.isdigit():
        if (int(sayi) == 1) or (int(sayi) == 2) or (int(sayi) == 3) or (int(sayi) == 4):
            if int(sayi) == 1:
                if len(hesaplar) < 1:
                    print("Kayıtlı hiçbir hesap yoktur. Lütfen kaydolunuz.")
                else :
                    u1 = input("Lütfen Kullanıcı Adınız Giriniz: \n")
                    p1 = input("Lütfen Şifrenizi Giriniz: \n")
                    girisyap(u1,p1)


            elif int(sayi) == 2:
                x = hesapolustur()
                hesaplar.append(x)
                print("Hesabın başarıyla eklendi.")
                print(hesaplar)
            elif int(sayi) == 3:
                for x in range(len(hesaplar)):
                    y = x+1
                    print(y ,"- ",(hesaplar)[x])
                if len(hesaplar) < 1:
                    print("Kayıtlı hiçbir hesap yoktur.")
                else:
                    kindex= int(input("Kaç numaralı hesabı silmek istiyorsun?\n"))
                    wremove = kindex -1
                    if len(hesaplar) < kindex:
                        print(kindex , ". hesap yoktur. Lütfen başka bir hesap giriniz.")
                    hesaplar.pop(wremove)
            elif int(sayi) == 4:
                if len(hesaplar) < 1:
                    print("Kayıtlı hiçbir hesap yoktur.")
                else:
                    print("Hesaplar Listeleniyor.")
                    time.sleep(1)
                    print("Hesaplar Listeleniyor..")
                    time.sleep(1)
                    print("Hesaplar Listeleniyor...")
                    time.sleep(1)
                    for x in range(len(hesaplar)):
                        y = x + 1
                        print(y, "- ", (hesaplar)[x])
                    print("Hesaplar Listelendi.")

        else:
            print("Yanlış bir rakam girdin. Lütfen 1 veya 2 yaz!")
    else:
        print("Yanlış bir karakter girdin. Lütfen 1 veya 2 yaz!")
