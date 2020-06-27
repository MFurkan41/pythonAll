import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep as bekle
import sqlite3
import re
import os, sys

con = sqlite3.connect("emlakcilar.db")
cursor = con.cursor()

browser = webdriver.Chrome()

y=False

for m in range(1,50):
    browser.get("https://www.bulurum.com/dir/emlakcilar/istanbul/")
    for o in range(1,10):
        url = "https://www.bulurum.com/dir/emlakcilar/istanbul/?page="
        url += str(o)
        browser.get(url)
        for x in range(0, 20):
            try:
                a = browser.find_element_by_xpath("//*[@id='captchaWrapper']/div[1]")
            except:
                pass
            else:
                print("recaptcha!!!")
                try:
                    input("Press enter to continue...")
                    url = "https://www.bulurum.com/dir/emlakcilar/istanbul/?page="
                    url += str(o)
                    browser.get(url)
                except SyntaxError:
                    pass

            string = "//*[@id='FreeListingAreaRight_"
            string += str(x+7)
            string += "']/a[3]"
            try:
                browser.find_element_by_xpath(string).click()
            except:
                continue
            
            liste = list()
            isim = "//*[@id='CompanyNameLbl']/span/span"
            try:
                isim = browser.find_element_by_xpath(isim).text
            except:
                browser.back()
                continue
            while True:
                if(isim[0] == "-"):
                    try:
                        isim = isim.split("(")[1]
                    except:
                        liste.append("emlakci")
                        break
                    isim = isim[:-1]
                    liste.append(isim)
                elif(isim[0] == "("):
                    isim = isim[:-1]
                    isim = isim.replace("(","")
                    liste.append(isim)
                else:
                    liste.append("emlakci")
                    break
                break
            try:
                tel = "//*[@id='MobileContLbl']/span"
                tel = browser.find_element_by_xpath(tel).text
            except:
                browser.back()
                continue
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
                tel = str(tel.replace(" ",""))
                tel = int("90" + str(tel))
            liste.append(tel)
            
            try:
                cursor.execute("INSERT INTO emlakcilar (sirket_ismi, tel) VALUES (?,?)",(str(liste[0]),str(liste[1])))
                con.commit()
                print(liste)
            except sqlite3.IntegrityError:
                continue
            browser.back()
        
