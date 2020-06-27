sayi = input("Bir sayı Giriniz:")
bos = 0
birlik = ["Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
ondalik = ["On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
okunus = []
try:
    if int(sayi) < 100:
        for i in range (1,11):
            try:
                if birlik[i-1] in okunus:
                    bos+=1
                else:
                    if int(sayi[1]) == i:
                        okunus.append(birlik[i-1])
            except IndexError:
                pass
            for a in range (1,11):
                try:
                    if ondalik[a-1] in okunus:
                        bos +=1
                    else:
                        if int(sayi[0]) == a:
                            okunus.append(ondalik[a-1])
                except IndexError:
                    pass
    else:
        print("Lürfen 2 basamaklı bir sayı yazınız.")
        pass
except IndexError:
    pass
try:
    print(okunus[0],okunus[1])
except IndexError:
    print(okunus[0])
    pass
