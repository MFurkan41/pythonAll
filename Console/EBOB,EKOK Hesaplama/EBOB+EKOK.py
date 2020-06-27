print("EBOB : 1,\nEKOK : 2\n")
a = int(input())
if(a == 1):
    def bolenler(sayi):
        bolenler=[]
        for i in range(1,sayi+1):
            if(sayi % i == 0):
                bolenler.append(i)
        return bolenler
    sayi1 = int(input("Bir sayı Giriniz: "))
    sayi2 = int(input("Bir sayı Daha Giriniz: "))
    sayi1 = bolenler(sayi1)
    sayi2 = bolenler(sayi2)
    sonuc = []
    for i in range(0,len(sayi1)):
        for a in range(0, len(sayi2)):
            if sayi1[i] == sayi2[a]:
                sonuc.append(sayi1[i])
    print("EBOB: ",max(sonuc))
elif(a == 2):
    def katlar(sayi):
        skatlar = []
        for i in range(1,11):
            skatlar.append(sayi*i)
        return skatlar
    sayi1a = int(input("Bir sayı Giriniz: "))
    sayi2a = int(input("Bir sayı Daha Giriniz: "))
    sayi1 = katlar(sayi1a)
    sayi2 = katlar(sayi2a)
    ekok = []
    for i in range(0,len(sayi1)):
        for a in range(0,len(sayi2)):
            if sayi1[i] == sayi2[a]:
                ekok.append(sayi2[a])
    try:
        print(min(ekok))
    except ValueError:
        print("EKOK: ",(sayi1a*sayi2a) )
