liste = [23,45,78,12,44,27,37,41,93,55,82,34,15]
def ciftmi(sayi):
    if (sayi % 2 == 0):
        return True
    if (sayi % 2 == 1):
        return False
ciftler = []
tekler = []
for i in range(0,len(liste)):
    if(ciftmi(liste[i]) == True):
        ciftler.append(liste[i])
    elif(ciftmi(liste[i]) == False):
        tekler.append(liste[i])
print(ciftler)