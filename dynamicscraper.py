import selenium
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get('https://www.dohop.com/flights/BLR/DEL/2019-10-12/adults-1?stops=0#transfer-step/G8118-BLR-DEL-10-12')

res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup = BeautifulSoup(res, 'lxml')

box = soup.find('div', {'class': 'VendorPicker'})
prices = box.find_all('div', {'class': 'VendorTile'})

for price in prices:
    p = price.find('div',{'class':'VendorTile--fadeIn'})
    print(p)
    print(p.text)