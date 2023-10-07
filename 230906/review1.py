import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
result = soup.find("h2") 
#<h2>이곳은 크롤링 연습을 위한 웹사이트입니다.</h2>

print(result.text)

