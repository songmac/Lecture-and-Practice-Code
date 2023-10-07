import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/02')
soup = BeautifulSoup(res.text, 'html.parser')

all = []
result = soup.select("body > a")  #리스트 타입
for value in result:
    #print(value)
    com = value.text
    url = value.attrs["href"]
    #print(type(com))  #str
    #print(type(url))  #str
    all.append([com, url])
print(all)