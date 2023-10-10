import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
result = soup.find(id="hello")
#이탈리아 요리의 시작은 기원전 4세기로 거슬러 올라갈 수 있다. 대항해시대를 거치면서 아메리카 대륙에서 감자·토마토·후추·옥수수 등이 유입되어 그 종류와 풍미가 다양해졌고 현대에 이르러서는 피자와 파스타 등 많은 이탈리아 요리가 널리 퍼지게 되었다.

print(result.text.strip())

