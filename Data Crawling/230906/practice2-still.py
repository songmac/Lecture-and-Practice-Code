import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/03')
soup = BeautifulSoup(res.text, 'html.parser')


"""인기검색종목-종목명과 상한, 하한 여부"""
raw_data = soup.select(".lst_pop > li") 

final_results = []
for n in raw_data:
    upper = n.select("img > alt")
    #upper = n.select("img > alt")[0].text.strip()  
    #final_results.append([pop_list, number])
    print(upper)
#print(final_results)
    

"""주요 해외 지수-종목명과 상한, 하한 여부"""
#raw_data2 = soup.select(".lst_major > li") 

#final_results2 = []
#for n2 in raw_data2:  
#    major_list = n2.select("a")[0].text.strip()
#    number2 = n2.select("span")[0].text.strip()
#    final_results2.append([major_list, number2])
#print(final_results2)