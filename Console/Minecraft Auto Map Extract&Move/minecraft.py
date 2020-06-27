import zipfile
import glob
import os, os.path
import shutil
from tqdm import tqdm
from time import sleep as bekle

globname = str(os.getlogin())
list_of_files = glob.glob('c:/users/' + globname + '/downloads/*')
latest_file = max(list_of_files, key=os.path.getctime)
latest_file = latest_file.replace(chr(92),"/")
print("Yüklenilen haritanın zip dosyası : " + latest_file.split("/")[4])

with zipfile.ZipFile(latest_file) as zf:
    for member in tqdm(zf.infolist(), desc='Zip açılıyor... '):
        try:
            zf.extract(member, "C:/Users/" + globname + "/AppData/Roaming/.minecraft/saves")
        except zipfile.error as e:
            pass

print("Harita Yüklendi!")
bekle(1)
wclean = glob.glob("C:/Users/" + globname + "/AppData/Roaming/.minecraft/saves" + "/*.*")
print("-------------------------")
print("Gereksiz Dosyalar Siliniyor...")
for clean in wclean:
    clean = clean.replace(chr(92),"/")
    try:
        os.remove(clean)
    except PermissionError:
        pass
    finally:
        print("Gereksiz dosya silindi : " + str(clean.split("/")[7]))
bekle(3)


