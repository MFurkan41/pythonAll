import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep as bekle
import sqlite3
import re

con = sqlite3.connect("info.db")
cursor = con.cursor()

y = True

cursor.execute("SELECT * FROM site")
allacc = cursor.fetchall()
result = [re.sub(r'([0-9\.])\(.*?\n', r'\1', x[0]) for x in allacc]
    

browser = webdriver.Chrome()
browser.get("http://whois.domaintools.com/")

for i in range(1,270):
    liste = list()
    input_whois = browser.find_element_by_xpath("//*[@id='landing-whois']")
    input_whois.clear()
    input_whois.send_keys(str(result[i]))

    liste.append(str(result[i]))
    
    sorgula = browser.find_element_by_xpath("//*[@id='whois-search']").click()
    bekle(3)
    try:
        buy = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/a")
    except:
        y=False
    if(y == True):
        created_on = "süresi bitmiş"
        expires_on = "süresi bitmiş"
        dns = "süresi bitmiş"
    else:
        try:
            created_on = browser.find_element_by_xpath("//*[@id='stats']/table/tbody/tr[6]/td[2]/span[2]").text
            created_on = created_on[11:]
        except:
            pass
    
        try:
            expires_on = browser.find_element_by_xpath("//*[@id='stats']/table/tbody/tr[6]/td[2]/span[3]").text
            expires_on = expires_on[11:]
        except:
            pass
        
        try:
            dns = browser.find_element_by_xpath("//*[@id='stats']/table/tbody/tr[7]/td[2]/text()[1]").text
            dns = dns.replace(" ","")
            head, sep, tail = text.partition('(')
            dns = head
        except:
            pass
        
    liste.append(created_on)
    liste.append(expires_on)
    liste.append(dns)

    cursor.execute("INSERT INTO y_site VALUES (?,?,?,?)",(liste[0],liste[1],liste[2],liste[3]))
    con.commit()
    print(liste)
    browser.get("http://whois.domaintools.com/")

    

    
    
