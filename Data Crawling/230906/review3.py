import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

results = soup.find("tbody").find_all("tr")
#print(results)

students = []

for result in results:
    #print(result.find_all("td"))
    #print(result.find_all("td")[0])
    #print(result.find_all("td")[1])
    name = result.find_all("td")[0].text
    age = int(result.find_all("td")[1].text)
    students.append([name, age])
print(students)
    