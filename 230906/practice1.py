import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/03')
soup = BeautifulSoup(res.text, 'html.parser')


"""인기검색종목"""
raw_data = soup.select(".lst_pop > li") #'>'양쪽에 공백이 있어야 함
#print(results)

#pop_list = soup.select("a")
#print(pop_list)
#print(pop_list[0]) #써니전자

#number = soup.select("span")
#print(number)
#print(number[0])

#a = [0]
#a[0] #리스트 안의 값만 출력!!!

final_results = []
for n in raw_data:  #print(n) => li
    pop_list = n.select("a")[0].text.strip()  #리스트'[]' 밖에서는 text를 추출할 수 없음
    number = n.select("span")[0].text.strip()
    #print(pop_list)
    #print(number)
    final_results.append([pop_list, number])
print(final_results)

#print(bs.select_one('#title').text.strip())


"""주요 해외 지수"""
raw_data2 = soup.select(".lst_major > li") 

final_results2 = []
for n2 in raw_data2:  
    major_list = n2.select("a")[0].text.strip()
    number2 = n2.select("span")[0].text.strip()
    final_results2.append([major_list, number2])
print(final_results2)