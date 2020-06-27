from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://www.tongucakademi.com/login")

loginMail = browser.find_element_by_xpath("//*[@id='LoginEmail']")
loginMail.clear()
loginMail.send_keys("fyolal2006@gmail.com")

loginPass = browser.find_element_by_xpath("//*[@id='LoginSifre']")
loginPass.clear()
loginPass.send_keys("SulMeh44.")

time.sleep(1)

loginButton = browser.find_element_by_xpath("//*[@id='GirisButton']")
loginButton.click()

time.sleep(2)

matButton = browser.find_element_by_xpath("/html/body/section/div[4]/div/div[2]/ul/li[2]/a")
matButton.click()

time.sleep(2)

tamButton = browser.find_element_by_xpath("/html/body/section/div[2]/div/div/div/ul/li[1]/a")
tamButton.click()

time.sleep(2)

dersButton = browser.find_element_by_xpath("/html/body/section/div[2]/div/div[2]/div[1]/ul/li[1]/a")
dersButton.click()
