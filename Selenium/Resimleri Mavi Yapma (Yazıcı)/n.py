from selenium import webdriver
from time import sleep as bekle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os, os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import glob
import shutil


#C:/Users/mfurk/Desktop/Inkılap



path = input("yol : ")
fpath = str(path) + "/filtered"
try:
    os.mkdir(fpath)
except FileExistsError:
    shutil.rmtree(fpath)
    os.mkdir(fpath)
fpath = fpath.replace(chr(92),"/")

browser = webdriver.Chrome()
browser.get("https://www.imgonline.com.ua/eng/color-filter.php")
fcount = (len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]))



for i in range(0,fcount):
    a = "00" + str(i+1)
    if(len(a) == 3):
        a = "0" + str(a)
    a = a + ".jpg"
    text = "C:/Users/mfurk/Desktop/Inkılap/" +str(a)
    upload_box = browser.find_element_by_name("uploadfile")
    upload_box.send_keys(text)

    browser.find_element_by_xpath("//*[@id='content']/form/div[2]/table/tbody/tr[3]/td[6]/input").click()

    browser.find_element_by_xpath("//*[@id='content']/form/div[4]/input").click()
    bekle(3)
    
    browser.find_element_by_xpath("//*[@id='content']/a[2]").click()
    bekle(2)
    while True:
        try:
            list_of_files = glob.glob('c:/users/mfurk/downloads/*.jpg')
            latest_file = max(list_of_files, key=os.path.getctime)
            latest_file = latest_file[25:]
            os.rename("c:/users/mfurk/downloads/" + str(latest_file),fpath + "/" + a)
        except PermissionError:
            continue
        break
    bekle(0.5)
    browser.get("https://www.imgonline.com.ua/eng/color-filter.php")
    
