from selenium import webdriver
import os
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.books.com.tw/?gad_source=1&gbraid=0AAAAAD4DKPxAbFeG_GYlvRRY1QqkRUwAj&gclid=Cj0KCQjwiLLABhCEARIsAJYS6umq00m-nNbrhbihBeBKJv8367coCpZbA_zlQmWfLbQcPlS6Nurinq0aAho_EALw_wcB'

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(url)
htmilfile = driver.page_source
img = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'dailywords-img'))
)

soup = BeautifulSoup(htmilfile)

imgs = soup.find_all('img')

print(imgs)

i = 1
for img in imgs:
    path = img.get_attribute('src')
    name = img.get_attribute('alt')
    source = requests.get(path)
    img_source = source.content
    os.makedirs('imges', exist_ok=True)

    with open(f'imges{name}.jpg','wb') as file:
        file.write(img_source)
