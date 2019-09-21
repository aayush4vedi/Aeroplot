import time
import selenium
import requests
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import xlrd
import openpyxl 
from datetime import datetime

# 1.fetch flight-data from xlsx file

flights = []
dates   = []
froms   = []
tos     = []
urls    = []
prices  = []
fid     = []

fwb = xlrd.open_workbook("flights.xlsx")
sheet = fwb.sheet_by_index(0)

for i in range(1,sheet.nrows):
    fid.append(sheet.cell_value(i,0))
    dates.append(sheet.cell_value(i,1))
    flights.append(sheet.cell_value(i,4))
    froms.append(sheet.cell_value(i,5))
    tos.append(sheet.cell_value(i,6))


# 2. make urls

prefix = "https://www.google.com/flights?hl=en#flt=/m/09c17./m/0dlv0."
suffix = ";c:INR;e:1;sd:1;t:b;tt:o;sp:0.."
for i in range(0,2): # make 2nd value = len(fid)
    url = prefix + dates[i] + "." + froms[i] + tos[i] + "0" + flights[i] + suffix
    urls.append(url)

# 'periodic' scraping & storing in separete xlsx file

#store data in excel sheet
db = openpyxl.load_workbook('db.xlsx')
sheet = db.active
dateTimeObj = datetime.now()
entry = []
entry.append(dateTimeObj)
for i in range(0,len(urls)):
    url = urls[i]
    #print('url:', url)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(5)#make it 30 again
    res = driver.execute_script("return document.documentElement.outerHTML;")
    driver.quit()
    soup = BeautifulSoup(res, 'lxml')
    try:
        price = soup.find('div', {'class':'pSUwrf flt-headline1'})
        price = price.text[2:]
        print(price)
        prices.append(price[2:])
    except:
        price = prices[-1]
        prices.append(price)
        print('ERROR!')
    entry.append(price)

print('appending:', entry)
sheet.append(entry) 

db.save('db.xlsx')

#TODO: make it run houerly for x days
#TODO: make browsers inbuilt