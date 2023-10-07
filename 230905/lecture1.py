import requests
from bs4 import BeautifulSoup

URL ='https://crawlingstudy-dd3c9.web.app/01'

data ={
    'name':'jinbeom'
}

headers = {
    'Content-Type':'application.json;charset=utf-8'
}

response = requests.get(URL, headers=headers, data=data)

print(response.status_code)
#print(response.text)