import re

sentences = """
안녕하세요 저는 <em>홍길동</em> 입니다. 나이는 24살 세계 최고의 <a href="aa.aa.com">데이터 분석가</a>가 되고싶습니다.
""" 

sentences = re.sub("<[^>]*>", "", sentences)

print(sentences)