import time
from random import randint
x =(randint(1, 10))
can = 3
while can == 1 or can == 2 or can == 3: 
    xk = int(input("0-10 arasında bir sayı giriniz: \n"))
    s = x - xk
    if xk > 10:
        print("Lütfen 0-10 arasında bir sayı giriniz.")
    if xk < 0:
        print("Lütfen 0-10 arasında bir sayı giriniz.")
    if s > 0:
       can = can - 1
       print("Lütfen daha büyük bir sayı giriniz." , " Kalan can sayınız : " , can)
    elif s == 0: 
       print("Tebrikler kazandınız!")
       can = 10
    else:
       can = can - 1
       print("Lütfen daha küçük bir sayı giriniz." , " Kalan can sayınız : " , can)
    if can == 0:
        print("Malesef Kaybettiniz! Tekrar Deneyiniz.")
        can = 10
    if can == 10:
        print("Oyun Bitti.")
        time.sleep(3)
 
