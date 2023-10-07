import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/03')
soup = BeautifulSoup(res.text, 'html.parser')

box = soup.select("body > ul > li.sale_item div.sale_box")
box_detail = soup.select(".sale_detail")

#print(box[0:])
#print(box_detail)

#name(이름), price(분양가), type(유형), lease(분양유형), size(규모), space(면적)
for value in box[0:] :
    box_key = soup.select("dt")
    for value2 in box[0:] :
        box_value = soup.select("dd")
        print([box_key, box_value])




    #print(value)
    #name = value.select("a") #개별리스트
    #price = value.select(".point") #개별리스트
    #type = value.select(".sale_datail") """안됨"""
    #print(name)
    #print(price)
   # print(type) """안됨"""

    
    
    
    
    
    
    
    
    #point = data.select("dt.tit > dd.txt.point")
    

    #print (value)

    #for data in  :
    #    print(data)
    #    for data2 in name :
    #       print((index, point))









    #point = index.find("dd", class_= "point")
    #print(point)

    #url = value.attrs["href"]

#print(result)


