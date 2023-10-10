import requests
from bs4 import BeautifulSoup

URL ='https://crawlingstudy-dd3c9.web.app/01'

response = requests.get(URL)

bs = BeautifulSoup(response.text, 'html.parser')
result = bs.find(id='cook')

#print(result)
print(result.text)