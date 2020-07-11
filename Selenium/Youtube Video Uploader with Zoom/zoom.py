from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
import os, glob
from time import sleep as bekle

def clickButton(xpath):
    while True:
        try:
            browser.find_element_by_xpath(xpath).click()
        except (NoSuchElementException,ElementNotInteractableException):
            bekle(0.5)
            continue
        else:
            break

def enterInput(xpath, key):
    while True:
        try:
            element = browser.find_element_by_xpath(xpath)
            if(element.get_attribute("type") != "file"):
                bekle(0.5)
                element.clear()
                bekle(0.5)
                element.clear()
                for i in key:
                    element.send_keys(i)
            else:
                element.send_keys(key)
        except (NoSuchElementException,ElementNotInteractableException):
            bekle(0.5)
            continue
        else:
            break    


def latestSubdir(n=0,lenDir=None):
    if lenDir == True:
        return len(sorted(glob.glob(os.path.join("C:\\Users\\mfurk\\Documents\\Zoom\\", '*/')), key=os.path.getmtime))
    else:
        folder = sorted(glob.glob(os.path.join("C:\\Users\\mfurk\\Documents\\Zoom\\", '*/')), key=os.path.getmtime)[-n]
        return folder.replace("\\","/")

def getText(xpath):
    while True:
        try:
            return browser.find_element_by_xpath(xpath).text
        except (NoSuchElementException, ElementNotInteractableException):
            bekle(0.5)
            continue
        else:
            break


kisim = 2

konu = ["Temel Python Objeleri ve Veri Yapıları",
        "Döngüler",
        "Koşullu Durumlar",
        "Fonksiyonlar",
        "Modüller",
        "Nesne Tabanlı Programlama",
        "Dosya İşlemleri",
        "Hatalar ve İstisnalar",
        "Pythondaki Gömülü Fonksiyonlar",
        "İleri Seviye Veri Yapıları ve Objeler",
        "Sqlite Veritabanı",
        "Pythondaki Decoratorlar",
        "Pythondaki Iteratorlar ve Generatorlar",
        "İleri Seviye Modüller"]

ters = [*range(1,int(kisim)+1)][::-1]

browser = webdriver.Chrome()
browser.get("https://studio.youtube.com/channel/UC1a1vJlzs4pg6wSwzCSf8pw/videos/upload?d=ud&filter=%5B%5D&sort=%7B'columnType'%3A'date'%2C'sortOrder'%3A'DESCENDING'%7D")

browser.maximize_window()

print("\nYouTube Açıldı! \n------------")

enterInput("//*[@id='identifierId']","yolalacademy@gmail.com")
clickButton("//*[@id='identifierNext']/div")
enterInput("//*[@id='password']/div[1]/div/div[1]/input","YAcademy12**")
clickButton("//*[@id='passwordNext']/div")

print("\nGiriş Yapıldı!\n\n------------")

for i in range(int(kisim)):
    enterInput("//*[@id='content']/input", latestSubdir(ters[i])+"zoom_0.mp4")

    video_ismi = "Python Dersleri " + str(latestSubdir(lenDir=True) // 2) + "." + str(i+1) + " ( " + konu[latestSubdir(lenDir=True) // 2 - 1] + " )"

# //*[@id='checkbox-label-0']

    print("\n----------\n" + str(i+1) + ". video yükleniyor...")
    print("Video İsmi : " + video_ismi)
    print("Video Yolu : " + latestSubdir(ters[i]) + "zoom_0.mp4")

    #Başlık
    enterInput("/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-mention-textbox[1]/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div",video_ismi)
    # Açıklama
    enterInput("/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-mention-textbox[2]/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div",video_ismi)
    # Oynatma Listesi
    clickButton("//*[@id='basics']/ytcp-video-metadata-playlists/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger")
    # Oynatma Listesi Kontrol

    for j in range(3):
        if ("Python" in getText("//*[@id='checkbox-label-" + str(j) +"']/span")):
            clickButton("//*[@id='checkbox-label-"+str(j)+"']")

    clickButton("//*[@id='dialog']/div[2]/ytcp-button[3]/div")
    # Çocuklar için Değil
    clickButton("//*[@id='made-for-kids-group']/paper-radio-button[2]")
    # İleri
    clickButton("//*[@id='next-button']/div")
    # İleri
    clickButton("//*[@id='next-button']/div")
    # Liste Dışı
    clickButton("//*[@id='privacy-radios']/paper-radio-button[2]")
    # Kaydet
    clickButton("//*[@id='done-button']")
    #Kapat
    clickButton("//*[@id='close-button']/div")
    if(i != list(range(int(kisim)))[-1]):
        print("Video Yüklendi! Sıradakine geçiliyor...")
        # New Video Upload
        clickButton("//*[@id='create-icon']")
        # Upload
        clickButton("//*[@id='text-item-0']")
print("Tüm videolar yüklendi! 5 dk içinde kapanacak.")
bekle(300)
browser.close()
