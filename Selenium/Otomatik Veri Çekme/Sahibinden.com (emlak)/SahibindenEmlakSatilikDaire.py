import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep as bekle
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sqlite3
import re
import os, sys

con = sqlite3.connect("emlakcilar.db")
cursor = con.cursor()

browser = webdriver.Chrome()
browser.get("https://www.sahibinden.com/emlak-konut?a27=38461")

for i in range(2,24922):
    for x in range(1, 20):
        
        string = "#searchResultsTable > tbody > tr:nth-child("
        string += str(x)
        string += ") > td.searchResultsTitleValue > a.classifiedTitle"
        element=browser.find_element_by_xpath(string)
        ActionChains(browser).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
        browser.switch_to.window(browser.window_handles[1])
        """browser.find_element_by_xpath(string).click()"""
            
        liste = list()
        isim = "//*[@id='classifiedDetail']/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/a/span/span"
        isim = browser.find_element_by_xpath(isim).text
        liste.append(isim)

        tel = "//*[@id='phoneInfoPart']/li/span[1]"
        tel = browser.find_element_by_xpath(tel).text
        liste.append(tel)
            
        adres = "//*[@id='classifiedDetail']/div[1]/div[2]/div[2]/h2/a[1]"
        adres = browser.find_element_by_xpath(adres).text
        liste.append(adres)
        cursor.execute("INSERT INTO emlakcilar (sirket_ismi,tel,adres) VALUES (?,?,?)",(str(liste[0]),str(liste[1]),str(liste[2])))
        con.commit()
        print(liste)

        browser.close()
        continue
            
        browser.switch_to.window(browser.window_handles[0])

        

    url = "//*[@id='searchResultsSearchForm']/div/div[3]/div[3]/div[1]/ul/li["
    url += str(i+1)
    url += "]/a"
    url = browser.find_element_by_xpath(url).click()  
