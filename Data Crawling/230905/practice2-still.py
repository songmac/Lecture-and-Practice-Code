import requests
from bs4 import BeautifulSoup
res = requests.get('https://crawlingstudy-dd3c9.web.app/01/')

bs = BeautifulSoup(res.text, 'html.parser')

for data in bs.select("thead > tr > th.tablehead"):
    data = data
    print(data)
# print(bs.select("thead > tr > th.tablehead")[0])
# print(bs.select("thead > tr > th.tablehead")[1])

# print(bs.select("tbody > tr > td")[0])
# print(bs.select("tbody > tr > td")[1])
# print(bs.select("tbody > tr > td")[2])
# print(bs.select("tbody > tr > td")[3])


"""body > thead > tr"""
"""body > tbody > td (2번 반복)"""