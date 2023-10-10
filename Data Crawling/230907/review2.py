import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/02')
soup = BeautifulSoup(res.text, 'html.parser')

result = soup.select("div#content > ul > li.blue")
for list in result:
    print(list.text)

#print(result)
