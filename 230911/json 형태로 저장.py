import json
import requests
from bs4 import BeautifulSoup

res = requests.get("https://jsonplaceholder.typicode.com/posts")
result_dic = json.loads(res.text)

with open("data.json", "w") as json_file:
    json.dump(result_dic, json_file)

with open("data.json", "r") as json_file:
    result = json.load(json_file)

print(result)

# for data in result_dic : 
#     print(data)