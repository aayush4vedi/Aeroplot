import selenium
import requests
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

flights = ["G8113","6E2625"]
dates   = ["2019-09-27","2019-09-27"]
froms   = ["DEL","BLR"]
tos     = ["BLR","DEL"]


i=0
urls = []
#making urls from www.dohop.com
prefix = "https://www.dohop.com/flights"
mid = "adults-1?stops=0#transfer-step"
while i < len(flights):
    url = prefix + "/" + froms[i] + "/" + tos[i] + "/" + dates[i] + "/" + mid + "/" + flights[i] + "-" + froms[i] + "-" + tos[i] + "-" + dates[i][5:]
    urls.append(url)
    i += 1
# print(urls)

for url in urls:
    print('url:', url)
    driver = webdriver.Chrome()
    driver.get(url)
    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    soup = BeautifulSoup(res, 'lxml')
    try:
        box = soup.find('div', {'class': 'VendorPicker'})
        prices = box.find_all('div', {'class': 'VendorTile'})
        for price in prices:
            p = price.find('div',{'class':'VendorTile--fadeIn'})
            print(p.text)
    except:
        print('ERROR!')
