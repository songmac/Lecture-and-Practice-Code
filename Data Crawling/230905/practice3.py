import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/01/')

bs = BeautifulSoup(res.text, 'html.parser')

for link in bs.find_all('a'):
    link = 'https://crawlingstudy-dd3c9.web.app/01/' +link.attrs["href"]   #핵심문장
    # print(link)
    # 01.html
    # 02.html
    # 03.html
    # 04.html

    sub_res = requests.get(link)
    sub_page = BeautifulSoup(sub_res.text, 'html.parser')
    print(sub_page.find("p").text.strip())
