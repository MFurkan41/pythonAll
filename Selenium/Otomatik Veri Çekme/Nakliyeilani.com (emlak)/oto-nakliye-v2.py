import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
import time
import sqlite3
import re

con = sqlite3.connect("nakliyeciler.db")
cursor = con.cursor()
bad_chars = [';', ':', '!', "*", "&", "+","^","@"]
bad_chars2 = [';', ':', '!', "*", "&", "+","^","@"," "]
#https://www.nakliyeilani.com/ilceler-nakliye/34/Istanbul-yurtici-nakliye
browser = webdriver.PhantomJS()
url_t = "https://www.nakliyeilani.com/nakliye-firmalari-yurtici/1/34/443/Gungoren-nakliye"
browser.get(url_t)

try:
    cursor.execute("CREATE TABLE nakliyeciler (sirket_ismi TEXT,yetkili_kisi TEXT, is_tel TEXT, cep_tel TEXT, fax TEXT)")
except sqlite3.OperationalError:
    pass
liste = list()

window_before = browser.window_handles[0]
fl = range(1,130)
for i in fl:
    url = "https://www.nakliyeilani.com/nakliye-firmalari-yurtici/"
    url += str(i)
    url += "/34/443/Gungoren-nakliye"
    browser.get(url)
    follow_loop = range(1, 6)
    
    for j in follow_loop:
        site = "//*[@id='aspnetForm']/div[4]/div[2]/div/table["
        site += str(j)
        site += "]/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/table/tbody/tr[4]/td[3]/a"
        site = browser.find_element_by_xpath(site)
        site.click()
        time.sleep(4)
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        """
        try:
            sirket_ismi = browser.find_element_by_xpath("//*[@id='aspnetForm']/div[4]/div[2]/table[2]/tbody/tr/td[1]/table/tbody/tr[1]/td").text
        except:
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
            continue
        sirket_ismi = sirket_ismi.strip()
        sirket_ismi = sirket_ismi.replace("\n", "")
        sirket_ismi = ''.join(i for i in sirket_ismi if not i in bad_chars) 
        liste.append(sirket_ismi)"""
        sahibi = browser.find_element_by_xpath("//*[@id='aspnetForm']/div[4]/div[2]/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[4]")
        sahibi = sahibi.get_attribute("innerHTML")
        sahibi = sahibi.strip()
        sahibi = sahibi.replace("\n", "")
        sahibi = ''.join(i for i in sahibi if not i in bad_chars)

        liste.append(sahibi)
    
        follow_loop = range(2, 5)
        for x in follow_loop:
            if(x == 2 or x == 4):
                continue
            tel = "//*[@id='aspnetForm']/div[4]/div[2]/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr["
            tel += str(x)
            tel += "]/td[3]"
            tel_real = browser.find_element_by_xpath(tel)
            text = tel_real.get_attribute("innerHTML")
            text = text.strip()
            text = text.replace("\n", "")
            text = ''.join(i for i in text if not i in bad_chars2)
            try:
                text = str(text)
            except ValueError:
                pass
            if(text == ""):
                print(end="")
                continue
            elif(text[0]=="+"):
                text = text[3:]
                text = text.replace("(","")
                text = text.replace(")","")
                text = text.replace("-","")
                text = text.replace(" ","")
                liste.append(text)
            elif(text[0] == "0"):
                text = text[1:]
                text = text.replace("(","")
                text = text.replace(")","")
                text = text.replace("-","")
                text = text.replace(" ","")
                liste.append(text)
            
        print(liste)
        try:
            cursor.execute("INSERT INTO nakliyeciler VALUES (?,?)",(liste[0],liste[1]))
        except IndexError:
            print("-Tel Yok")
            print(end="\n")
        con.commit()
        liste = list()
        browser.close()
        browser.switch_to.window(window_before)


