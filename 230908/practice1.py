import re

emails = """
jkilee@gmail.com
kttredef@naver.com
akdef!aa.com
adekik@best.kr
abkereff@aacde
adefgree@korea.co.kr
""" 

results = re.finditer("[A-Za-z]+\@+[A-Za-z]+\.([a-z]){3,4}", emails)

for result in results:
    print(result.group())
