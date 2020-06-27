from selenium import webdriver
from time import sleep as bekle
import sqlite3
import pyautogui as pg
from selenium.webdriver.common.action_chains import ActionChains

def clickbutton(xpath):
    browser.find_element_by_xpath(str(xpath)).click()

def enterinput(xpath,key):
    browser.find_element_by_xpath(str(xpath)).send_keys(str(key))

def switch_NW(c):
    if(c == True):
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
    else:
        browser.switch_to.window(browser.window_handles[len(browser.window_handles)-1])


baglanti = sqlite3.connect("database.db")
cursor = baglanti.cursor()

"""
cursor.execute("Create Table If not exists datas (data_name TEXT)")
baglanti.commit()
"""

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http://10.248.69.60/TTTESTWIKI/adm/index.php?i=acp_forums&sid=eb7d1e6939ae9e2063d6a0d997ff3dd8&icat=6&mode=manage&parent_id=5")

actions = ActionChains(browser)

cursor.execute("SELECT * FROM datas")
data = cursor.fetchall()

clickbutton("//*[@id='nav-main']/li[3]/a")
enterinput("//*[@id='username']",'admin')
enterinput("//*[@id='password']","Mehmet12")
bekle(1)
clickbutton("//*[@id='login']/div[1]/div/div/fieldset/dl[4]/dd/input[3]")
bekle(1)
clickbutton("//*[@id='nav-main']/li[3]/a")
pg.click(509,476)
actions.send_keys('Mehmet12')
actions.perform()
bekle(1)
clickbutton("//*[@id='login']/div/div/div/fieldset/dl[3]/dd/input[3]")

#BB
clickbutton("//*[@id='tabs']/ul/li[2]/a")
clickbutton("//*[@id='main']/div/table/tbody/tr[2]/td[2]/strong/a")
clickbutton("//*[@id='main']/div/table/tbody/tr[2]/td[2]/strong/a")

for i in range(0,len(data)):
    deger = str(data[i])
    deger = deger[2:]
    deger = deger[:-3]
    enterinput("//*[@id='forums']/fieldset/input[2]",deger)
    clickbutton("//*[@id='forums']/fieldset/input[3]")
    bekle(1)
    clickbutton("//*[@id='submit']")
    clickbutton("//*[@id='main']/div/div/p/a")

