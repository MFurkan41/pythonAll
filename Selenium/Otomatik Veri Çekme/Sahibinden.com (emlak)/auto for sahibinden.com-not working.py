import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep as bekle
import sqlite3
import re
import os, sys

con = sqlite3.connect("emlakcilar.db")
cursor = con.cursor()

browser = webdriver.Firefox()

browser.get("https://www.sahibinden.com/emlak-konut?a27=38461")
browser.find_element_by_xpath("//*[@id='searchResultsTable']/tbody/tr[1]/td[4]/a[1]").send_keys(Keys.CONTROL + 't')
browser.execute_script("window.open('');")
Window_List = browser.window_handles
browser.switch_to.window(Window_List[-1])

