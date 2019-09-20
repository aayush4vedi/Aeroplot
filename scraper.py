import selenium
import requests
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

flights = ["6E2625","G8118","G8118","SG6638"]
dates   = ["2019-09-27","2019-09-27","2019-09-28","2019-09-28"]
froms   = ["BLR","BLR","BLR","BLR"]
tos     = ["DEL","DEL","DEL","DEL"]


i=0
urls = []
#making urls
google_prefix = "https://www.google.com/flights?hl=en#flt=/m/0dlv0./m/09c17."
google_suffix = ";c:INR;e:1;sd:1;t:b;tt:o;sp:0"
while i < len(flights):
    #google flight
    gf_url = google_prefix + dates[i] + "." + froms[i] + tos[i] + "0" + flights[i] + google_suffix
    urls.append(gf_url)
    #make my trip
    # ixigo
    #other
    i += 1

# driver = webdriver.Chrome()

for url in urls: 
    print('opening: ', url)
    # webpage = requests.get(url)
    # content = webpage.content
    content = urllib2.urlopen(url)
    soup = BeautifulSoup(content)
    try:
        price = soup.findAll("div", attrs={"class": "pSUwrf"})
        print("price is:",price.text)
    except:
        print("can't open")

