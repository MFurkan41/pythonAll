import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep as bekle
import sqlite3
import re

con = sqlite3.connect("info.db")
cursor = con.cursor()

y = False

cursor.execute("SELECT * FROM site")
allacc = cursor.fetchall()
result = [re.sub(r'([0-9\.])\(.*?\n', r'\1', x[0]) for x in allacc]
    

browser = webdriver.Chrome()
bekle(10)

for i in range(1,270):
    browser.get("https://www.natro.com/domain-sorgulama/whois-sorgulama/sonuc")
    liste = list()
    input_whois = browser.find_element_by_xpath("//*[@id='domain-text']")
    input_whois.clear()
    input_whois.send_keys(str(result[i]))

    liste.append(str(result[i]))
    
    sorgula = browser.find_element_by_xpath("//*[@id='searchDomain']/div/span/button").click()
    bekle(5)
    try:
        created = browser.find_element_by_xpath("//*[@id='importantDateContent']/div[2]")
    except:
        y=True
    if(y == True):
        created_on = "süresi bitmiş"
        expires_on = "süresi bitmiş"
        dns = "pasif"
    else:
        created_on = browser.find_element_by_xpath("//*[@id='importantDateContent']/div[2]").text
        expires_on = browser.find_element_by_xpath("//*[@id='importantDateContent']/div[6]").text
        dns = "aktif"

        
    liste.append(created_on)
    liste.append(expires_on)
    liste.append(dns)

    cursor.execute("INSERT INTO y_site VALUES (?,?,?,?)",(liste[0],liste[1],liste[2],liste[3]))
    con.commit()
    print(liste)


    

    
    
