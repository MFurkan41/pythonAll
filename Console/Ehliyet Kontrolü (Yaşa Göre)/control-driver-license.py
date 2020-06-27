import time
#Ehliyet
yil = int(input("Dogum Yilinizi Giriniz: \n"))
x = False

if yil > 2019:
    print("Lütfen" , yil ," sayısından daha küçük bir sayı giriniz.")
    x = False
if yil < 1950:
    print("Lütfen" , yil ," sayısından daha büyük bir sayı giriniz.")
    x = False
if 1950 <= yil <= 2018:
    x = True
if x == True:
    yas = 2018 - yil
    kalan = 18 - yas
    if yas >= 18 :
        print("Ehliyet Alabilirsiniz.")
    if yas < 18 :
        print("Malesef Ehliyet Alamazsiniz." , kalan , " yil beklemeniz gerekmektedir.")
time.sleep(5)
