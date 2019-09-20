import requests
from bs4 import BeautifulSoup

url = "https://www.dohop.com/flights/BLR/DEL/2019-10-12/adults-1?stops=0#transfer-step/G8118-BLR-DEL-10-12"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

for i in soup.find_all("div", {"class": "TransferStepHeader__txt"}):
    print(i.text)