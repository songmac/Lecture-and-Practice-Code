import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/02')
soup = BeautifulSoup(res.text, 'html.parser')

result = soup.find(id="title")
print(result.text.strip())
