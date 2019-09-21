import time
import selenium
import requests
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import xlrd

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
# prefix = "https://www.dohop.com/flights"
# mid = "adults-1?stops=0#transfer-step"
prefix = "https://www.google.com/flights?hl=en#flt=/m/09c17./m/0dlv0."
suffix = ";c:INR;e:1;sd:1;t:b;tt:o;sp:0.."
for i in range(0,4):
#     url = prefix + "/" + froms[i] + "/" + tos[i] + "/" + dates[i] + "/" + mid + "/" + flights[i] + "-" + froms[i] + "-" + tos[i] + "-" + dates[i][5:]
    url = prefix + dates[i] + "." + froms[i] + tos[i] + "0" + flights[i] + suffix
    urls.append(url)

print('#urls:' , len(urls))

# 'periodic' scraping & storing in separete xlsx file
for url in urls:
    print('url:', url)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(30)
    res = driver.execute_script("return document.documentElement.outerHTML;")
    driver.quit()
    soup = BeautifulSoup(res, 'lxml')
    try:
        print('========================================')
        # box = soup.find('div', {'class': 'VendorPicker'})
        # prices = box.find_all('div', {'class': 'VendorTile'})
        # for price in prices:
        #     p = price.find('div',{'class':'VendorTile--fadeIn'})
        #     print(p.text)
        #     prices.append(p)
        price = soup.find('div', {'class':'pSUwrf flt-headline1'})
        print(price.text)
        prices.append(price.text)
    except:
        #entered price = NA
        print('ERROR!')

print('len of prices:' , len(prices))
for i in range(0,len(prices)):
    print('***********')
    print('flight-id:',fid[i] , 'price:', prices[i])

