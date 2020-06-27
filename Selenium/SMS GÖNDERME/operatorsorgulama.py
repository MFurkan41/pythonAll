from selenium import webdriver
from openpyxl import load_workbook
from time import sleep as bekle
from selenium.webdriver.common.keys import Keys


driver = webdriver.PhantomJS()
driver.get('https://www.turkiye.gov.tr/btk-numara-tasima')

filepath = "C:/Users/mfurk/Desktop/deneme.xlsx"
phone_column = "B"
phone_numbers = []

workbook = load_workbook(filename=filepath, read_only=True)
worksheet = workbook.active

for i in range(1000000):
    cell = "{}{}".format(phone_column, i+1)
    number = worksheet[cell].value
    if number == "None" or number is None:
        break
    if number != "" or number is not None: 
        phone_numbers.append(str(number))


for a in range(len(phone_numbers)):
    sorgulama = driver.find_element_by_xpath("//*[@id='txtMsisdn']")
    sorgulama.clear()
    numara = str(phone_numbers[a])
    numara = numara[2:]
    sorgulama.send_keys(phone_numbers[a])
    
    submit = driver.find_element_by_xpath("//*[@id='pageContentBlock']/section[2]/form/div/input[1]")
    submit.click()

    rawOperator = driver.find_element_by_xpath("//*[@id='pageContentBlock']/section[2]/div/text()")
    operator = rawOperator.split(" ")[]
