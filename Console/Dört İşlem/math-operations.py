import time

islem = input("Hangi işlemi yapmak istiyorsunuz? \n 1- Toplama \n 2- Çıkarma \n 3 - Çarpma \n 4 - Bölme \n İşleminiz : ")
if islem == "Toplama" or islem == "toplama":
    kac1 = int(input("1. sayıyı yazınız:"))
    kac2 = int(input("2. sayıyı yazınız:"))
    toplam = kac1 + kac2
    print("Sonucunuz bulunuyor.")
    time.sleep(1)
    print("Sonucunuz bulunuyor..")
    time.sleep(1)
    print("Sonucunuz bulunuyor...")
    time.sleep(1)
    print("Sonucunuz bulundu!")
    time.sleep(1.5)
    print("Sonuç :" , toplam)
        
elif islem == "Çıkarma" or islem == "çıkarma" or islem == "cikarma":
    kac1 = int(input("1. sayıyı yazınız:"))
    kac2 = int(input("2. sayıyı yazınız:"))
    toplam = kac1 - kac2
    print("Sonucunuz bulunuyor.")
    time.sleep(1)
    print("Sonucunuz bulunuyor..")
    time.sleep(1)
    print("Sonucunuz bulunuyor...")
    time.sleep(1)
    print("Sonucunuz bulundu!")
    time.sleep(1.5)
    print("Sonuç :" , toplam)
elif islem == "Çarpma" or islem == "çarpma" or islem == "carpma":
    kac1 = int(input("1. sayıyı yazınız:"))
    kac2 = int(input("2. sayıyı yazınız:"))
    toplam = kac1 * kac2
    print("Sonucunuz bulunuyor.")
    time.sleep(1)
    print("Sonucunuz bulunuyor..")
    time.sleep(1)
    print("Sonucunuz bulunuyor...")
    time.sleep(1)
    print("Sonucunuz bulundu!")
    time.sleep(1.5)
    print("Sonuç :" , toplam)
elif islem == "Bölme" or islem == "bölme" or islem == "bolme":
    kac1 = int(input("1. sayıyı yazınız:"))
    kac2 = int(input("2. sayıyı yazınız:"))
    toplam = kac1 / kac2
    print("Sonucunuz bulunuyor.")
    time.sleep(1)
    print("Sonucunuz bulunuyor..")
    time.sleep(1)
    print("Sonucunuz bulunuyor...")
    time.sleep(1)
    print("Sonucunuz bulundu!")
    time.sleep(1.5)
    print("Sonuç :" , toplam)
else:
    print("Toplama,Çıkarma,Çarpma veya Bölme işlemlerinden birisini seçiniz.")


    
    
    
