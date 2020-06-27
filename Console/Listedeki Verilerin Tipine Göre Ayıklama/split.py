#Liste içindeki indexleri ayıklama(int,str gibi)

liste = ["345","sadas","324a","14","kemal","murat","sultan","123","314gh","mehmet"]
sayılar =[]
stringler =[]
for i in range(0,len(liste)):
    try:
        liste[i] = int(liste[i])
        sayılar.append(liste[i])
    except:
        stringler.append(liste[i])
        continue
print(stringler)