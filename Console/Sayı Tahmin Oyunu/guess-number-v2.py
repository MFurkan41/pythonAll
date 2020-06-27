import time
from random import randint
#Hangi sayılar arasından seçileceğini değiştirebilirsiniz.
max = 10
min = 0
i=0
x = False
x =(randint(min, max))
#can sayısını değiştirebilirsiniz ama diğerlerini değiştirmeyin
can = 3
can2 = 0
can = can2
can += 3

while can == can or can == can2 - i:
    i+=1
    xk = int(input("{0}  ile  {1}  arasında bir sayı giriniz: \n".format(min,max)))
    s = x - xk
    if xk > 10:
        print("Lütfen " ,min, " ile ",max, " arasında bir sayı giriniz: \n")
    if xk < 0:
        print("Lütfen " ,min, " ile ",max, " arasında bir sayı giriniz: \n")
    if s > 0:
       can = can - 1
       print("Lütfen daha büyük bir sayı giriniz." , " Kalan can sayınız : " , can)
    elif s == 0: 
       print("Tebrikler kazandınız!")
       x = True
    else:
       can = can - 1
       print("Lütfen daha küçük bir sayı giriniz." , " Kalan can sayınız : " , can)
    if can == 0:
        print("Malesef Kaybettiniz! Tekrar Deneyiniz.")
        print("Sayı: {0}".format(x))
        x = True
    if x == True:
        print("Oyun Bitti.")
        time.sleep(3)
 
