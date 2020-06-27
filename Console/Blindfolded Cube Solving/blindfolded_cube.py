liste = [["A","Q"],["B","M"],["C","I"],["D","E"],["F","L"],["G","X"],["H","R"],["J","P"],["K","U"],["N","T"],["O","V"],["S","W"]]
write = input("")
write = write.upper()
write = write.split(",")
for i in range(0,len(write)):
    for j in range(0,len(liste)):
        try:
            if(write[i] == liste[j][0]):
                liste.pop(j)
            elif(write[i] == liste[j][1]):
                liste.pop(j)
        except:
            pass
for a in liste:
    print(a)
