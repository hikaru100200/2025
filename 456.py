from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url ='https://www.nike.com/tw/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

link = driver.find_elements(By.LINK_TEXT,'女款')

link.click()


link2 = driver.find_elements(By,LINK_TEXT,"鞋款")

link2.click()

time.sleep(2)

info = driver.find_elements(By,CLASS_NAME,'product-card__info')
time.sleep(3)

for item in info:
    title = driver.find_elements(By,CLASS_NAME,'product-card__title')
    price = driver.find_elements(By,CLASS_NAME,'product-card__prise')
    Print(f'{title}:{price}')