from domain_class import *
from selenium import webdriver
from time import sleep as bekle
from selenium.webdriver.common.keys import Keys
import random
import string
import os
import pyautogui as pg
import shutil
import fileinput
import sys
from seleniumrequests import Chrome

def getPass(stringLength):
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    return str(''.join((random.choice(lettersAndDigits) for i in range(stringLength))))

def clickbutton(xpath):
    browser.find_element_by_xpath(str(xpath)).click()

def enterinput(xpath,key):
    browser.find_element_by_xpath(str(xpath)).send_keys(str(key))

def switch_NW(c):
    if(c == True):
        browser.close()
        browser.switch_to.window(browser.window_handles[1])
    else:
        browser.switch_to.window(browser.window_handles[len(browser.window_handles)-1])

def get_pixel_colour(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[i_x, i_y]

def replaceConf(fileToSearch,textToSearch,textToReplace):
    tempFile = open( fileToSearch, 'r+' )

    for line in fileinput.input( fileToSearch ):
        tempFile.write( line.replace( textToSearch, textToReplace ) )
    tempFile.close()

def copyPhp(source,target):
    shutil.copy(source, target)

def doubleClick(xpath):
    action.double_click(str(xpath)).perform()

def RespCode(domain):
    webdriver = Chrome()
    domain = "http://www." + str(domain)
    response = webdriver.request('GET', domain)
    response = str(response)[11:][:-2]
    webdriver.close()
    return response

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.internetbilisim.net/clientarea.php")
action = webdriver.common.action_chains.ActionChains(browser)

db_path = str(sys.argv[1])




#Login
enterinput("//*[@id='inputEmail']",'myolal@gmail.com')
enterinput("//*[@id='inputPassword']","Smfm1980**")
clickbutton("//*[@id='login']")
#Services
clickbutton("//*[@id='mCSB_1_container']/ul/li[2]/strong/a")
clickbutton("//*[@id='tableServicesList']/tbody/tr[1]/td[5]/a")
#Login to WHM
clickbutton("//*[@id='domain']/div[6]/form/input[5]")

switch_NW(False)
site = Create_Site()
site.save_info(1,db_path)
for i in range(0,site.read_info('row_count')):
    site = Create_Site()
    site.save_info(int(i)+1,db_path)

    clickbutton("//*[@id='account_functions_create_a_new_account']")

    zip_name = str(site.read_info('zip_file').split(chr(92))[-1])
    
    #Create Acc
    bekle(3)
    enterinput("//*[@id='domain']",site.read_info('domain'))
    bekle(1)
    browser.find_element_by_xpath("//*[@id='username']").send_keys(Keys.CONTROL + "a")
    browser.find_element_by_xpath("//*[@id='username']").send_keys(Keys.DELETE)
    enterinput("//*[@id='username']",site.read_info('username'))
    if(site.read_info('password') == ""):
        kPass = getPass(16)
        print(kPass)
        enterinput("//*[@id='password']",kPass)
        enterinput("//*[@id='password2']",kPass)
    else:
        enterinput("//*[@id='password']",site.read_info('password'))
        enterinput("//*[@id='password2']",site.read_info('password'))
    enterinput("//*[@id='contactemail']","info@" + site.read_info('domain'))
    clickbutton("//*[@id='pkgselect']/option[2]")
    bekle(2)
    clickbutton("//*[@id='submit']")
    clickbutton("//*[@id='newAccountSubmit']")
    switch_NW(True)


    #DB Create
    clickbutton("//*[@id='item_mysql_database_wizard']")
    enterinput("//*[@id='db']","db1")
    clickbutton("//*[@id='submit']")
    enterinput("//*[@id='user']","u1")
    enterinput("//*[@id='password']",kPass)
    enterinput("//*[@id='password2']",kPass)
    bekle(1)
    clickbutton("//*[@id='submit_new_user']")
    clickbutton("//*[@id='ALL']")
    clickbutton("//*[@id='btnNextStep']")
    clickbutton("//*[@id='home']")
    clickbutton("//*[@id='item_php_my_admin']")
    switch_NW(False)

    bekle(1)
    url = browser.current_url
    url = url[:-9] + "db_import.php?db=" + site.read_info('username') + '_db1'
    browser.get(url)
    #clickbutton("//*[@id='topmenu']/li[6]/a")
    bekle(3)
    absolute_file_path = os.path.abspath(site.read_info('sql_file'))
    enterinput("//*[@id='input_import_file']",absolute_file_path)
    bekle(2)
    ex = browser.find_element_by_xpath("//*[@id='buttonGo']")
    browser.execute_script("arguments[0].click();", ex)
    bekle(5)
    switch_NW(True)


    #Upload .zip
    clickbutton("//*[@id='item_file_manager']")
    switch_NW(False)
    enterinput("//*[@id='location']","public_html")
    clickbutton("//*[@id='btnGo']")
    clickbutton("//*[@id='action-upload']/a")
    switch_NW(False)
    enterinput("//*[@id='uploader_file_input']",site.read_info('zip_file'))
    browser.switch_to.window(browser.window_handles[3])
    while True:
        if(get_pixel_colour(325, 690) == (92, 184, 92)):
            break
        continue
    bekle(2)
    browser.close()
    browser.switch_to.window(browser.window_handles[2])
    clickbutton("//*[@id='action-refresh']/a")
    bekle(1)
    pg.click(721,460)
    bekle(1)
    clickbutton("//*[@id='action-extract']/a")
    clickbutton("//*[@id='extract']/div[3]/span/button[1]")
    bekle(10)
    pg.click(1363,838)
    for i in range(0,len(site.read_info('conf_number').split('-'))):
        sayi = int((site.read_info('conf_number').split('-')[i]))-1
        bekle(1)
        Sm_y = 410+(sayi*38)
        pg.doubleClick(715,Sm_y)
        bekle(1)

    clickbutton("//*[@id='action-delete']/a")
    try:
        clickbutton("//*[@id='deleteme']")
    except:
        pg.click(715,Sm_y)
        bekle(1)
        clickbutton("//*[@id='action-delete']/a")
        bekle(1)
        clickbutton("//*[@id='deleteme']")
    clickbutton("//*[@id='trash']/div[3]/span/button[1]")
    clickbutton("//*[@id='action-upload']/a")
    switch_NW(False)

    #Edit conf file

    raw_target = site.read_info('conf_file').split(chr(92))
    raw_target.pop(-1)
    for i in range(0,len(raw_target)):
        if(i == 0):
            target = str(raw_target[0]) + chr(92)
            target = target[:-1]
        else:
            target += chr(92) + str(raw_target[i])
    target = target[:-1]
    target += chr(92) + chr(92) + site.read_info('conf_name')
    copyPhp(site.read_info('conf_file'),target)
    #print("Username = 'usernamehere', db = 'dbhere', password = 'passwordhere'")

    replaceConf(target,'usernamehere', site.read_info('username') + '_u1')
    replaceConf(target,'dbhere', site.read_info('username') + '_db1')
    if(kPass is not None):
        replaceConf(target,'passwordhere', kPass)
    else:
        replaceConf(target,'passwordhere', site.read_info('password'))

    #Upload conf file
    enterinput("//*[@id='uploader_file_input']",target)
    browser.switch_to.window(browser.window_handles[3])
    while True:
        if(get_pixel_colour(325, 690) == (92, 184, 92)):
            break
        continue
    browser.close()
    browser.switch_to.window(browser.window_handles[2])
    switch_NW(True)
    os.remove(target)

    #Change PHP Version (in need)
    if(RespCode(site.read_info('domain'))[0] != "2"):
        clickbutton("//*[@id='item_multiphp_manager']")
        phpdomain = "//*[@id='rowSelector_"
        phpdomain += str(site.read_info('domain'))
        phpdomain += "']"
        clickbutton(phpdomain)

        clickbutton("//*[@id='selectPhpVersion']/option[text()='PHP 5.4 (ea-php54)']")
        clickbutton("//*[@id='btnDomainPhpApply']")
        browser.close()
    else:
        browser.close()





    
