#BeaulfulSoup 실습

import requests
from bs4 import BeautifulSoup

URL ='https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)

bs = BeautifulSoup(response.text, 'html.parser')
#result = bs.find('title')
#result = bs.find_all('th', 'tablehead')
#result = bs.find_all(Class_ = 'tablehead')
#result = bs.find_all('th', attrs={'class':'tablehead'})
#result = bs.find_all('th', attrs={'title':'welcome'})

#print(result)

#for element in result:
#    print(element)
#    print(element.text.strip())

#print(result.text)

result1 = bs.find("table")
result2 = bs.find("tbody")

print(result1)
print(result2)

