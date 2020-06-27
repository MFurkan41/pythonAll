import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep as bekle
import sqlite3
import re
import os, sys

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


con = sqlite3.connect("emlakcilar.db")
cursor = con.cursor()

browser = webdriver.Chrome()
y=False
for m in range(1,50):
    browser.get("https://www.bulurum.com/dir/emlakcilar/istanbul/")
    for o in range(1,10):
        for x in range(0, 20):
            string = "//*[@id='moreIcon_"
            string += str(x)
            string += "']"
            try:
                browser.find_element_by_xpath(string).click()
            except:
                bekle(30)
            
            liste = list()
            isim = "//*[@id='firstRow_"
            isim += str(x)
            isim += "']/div[1]/div/h2/a/span[1]"
            try:
                isim = browser.find_element_by_xpath(isim).text
            except:
                continue
            liste.append(isim)

            tel = "//*[@id='DetailsMoreListing_"
            tel += str(x)
            tel += "']/div[2]"
            tel = browser.find_element_by_xpath(tel).text

            tel_list = list()
            if(tel == ""):
                pass
            else:
                y = True
                for i in tel:
                    tel_list.append(i)
                if(tel_list[0] == "0"):
                    tel = tel[1:]
                if(tel_list[0] == "+"):
                    tel = tel[3:]
                    y=False
            if(y == False):
                tela = tel
            else:
                tela = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', tel)
            liste.append(tela)
        
            adres = "//*[@id='firstRow_"
            adres += str(x)
            adres += "']/div[2]/div[1]/div[2]"
            adres = browser.find_element_by_xpath(adres).text
            liste.append(adres)
            try:
                cursor.execute("INSERT INTO emlakcilar (sirket_ismi, tel, adres) VALUES (?,?,?)",(str(liste[0]),str(liste[1]),str(liste[2])))
                con.commit()
                print(liste)
            except sqlite3.IntegrityError:
                continue
        
        

        url = "//*[@id='pagerPlaceHolder']/div/div[2]/a["
        url += str(o)
        url += "]"
        url = browser.find_element_by_xpath(url).click()  
