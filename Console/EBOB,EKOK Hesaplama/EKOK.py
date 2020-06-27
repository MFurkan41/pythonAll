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