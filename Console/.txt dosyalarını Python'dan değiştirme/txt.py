def dosyayiyazdir(dosya_ismi):
    try:
        file = open(dosya_ismi,"r")
    except FileNotFoundError:
        file = open(dosya_ismi,"w")
    finally:
        file = open(dosya_ismi, "r")
    for i in range (0,100):
        print(file.readline(),end="")
    file.close()
def dosyayaekle(dosya_ismi,eklenecek):
    try:
        file = open(dosya_ismi,"a")
    except FileNotFoundError:
        file = open(dosya_ismi,"w")
    finally:
        file = open(dosya_ismi, "a")
    file.write(eklenecek)
    file.close()
dosyayiyazdir("deneme.txt")
