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
browser = webdriver.Firefox()
urlb = "https://www.nakliyeilani.com/nakliye-firmalari-yurtici/1/34/455/Zeytinburnu-nakliye"
browser.get(urlb)

finish = False
gen = 0
try:
    cursor.execute("DROP TABLE nakliyeciler")
except:
    pass
try:
    cursor.execute("CREATE TABLE nakliyeciler (sirket_ismi TEXT,yetkili_kisi TEXT, is_tel TEXT, cep_tel TEXT, fax TEXT)")
except sqlite3.OperationalError:
    pass
liste = ["--","--","--","--","--"]

window_before = browser.window_handles[0]
fl = range(1,130)
for i in fl:
    url = urlb[:55]
    url += str(i)
    url += urlb[56:]
    browser.get(url)
    follow_loop = range(1, 6)
    if(finish ==  True):
        break
    for j in follow_loop:
        site = "//*[@id='aspnetForm']/div[4]/div[2]/div/table["
        site += str(j)
        site += "]/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/table/tbody/tr[4]/td[3]/a"
        try:
            site = browser.find_element_by_xpath(site)
        except:
            finish = True
            break
        site.click()
        time.sleep(2)
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
    
        try:
            sirket_ismi = browser.find_element_by_xpath("//*[@id='aspnetForm']/div[4]/div[2]/table[2]/tbody/tr/td[1]/table/tbody/tr[1]/td").text
        except:
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
            continue
        sirket_ismi = sirket_ismi.strip()
        sirket_ismi = sirket_ismi.replace("\n", "")
        sirket_ismi = ''.join(i for i in sirket_ismi if not i in bad_chars) 
        liste[0] = sirket_ismi

        sahibi = browser.find_element_by_xpath("//*[@id='aspnetForm']/div[4]/div[2]/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[4]")
        sahibi = sahibi.get_attribute("innerHTML")
        sahibi = sahibi.strip()
        sahibi = sahibi.replace("\n", "")
        sahibi = ''.join(i for i in sahibi if not i in bad_chars)
        liste[1] = sahibi 
        
        gen+=1
        
        follow_loop = range(2, 5)
        for x in follow_loop:
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
            text_list = list()
            if(text == ""):
                pass
            else:
                y = True
                for i in text:
                    text_list.append(i)
                if(text_list[0] == "0"):
                    text = text[1:]
                if(text_list[0] == "+"):
                    text = text[3:]
                    y=False
            if(y == False):
                texta = text
            else:
                texta = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', text)
            liste[x] = texta
        print(liste)
        cursor.execute("INSERT INTO nakliyeciler VALUES (?,?,?,?,?)",(liste[0],liste[1],liste[2],liste[3],liste[4]))
        con.commit()
        liste = ["--","--","--","--","--"]
        browser.close()
        browser.switch_to.window(window_before)

print("\n\n Tüm nakliyeciler kaydedilmiştir. ", str(gen), " adet nakliyeci tüm bilgileriyle birlikte databasededir.")


