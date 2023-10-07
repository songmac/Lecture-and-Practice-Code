import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/sise/sise_quant.nhn")
soup = BeautifulSoup(res.text, 'html.parser')


"""품목명과 현재가를 크롤링해주세요.""" 
result = soup.select("body #contentarea tr")[0].text
print(result)

# for data in result : 
#     prod = data.select("td > a")
#     print(prod)
#     #value = data.select("td.number")
#     #print(prod)
#     #print(value)
