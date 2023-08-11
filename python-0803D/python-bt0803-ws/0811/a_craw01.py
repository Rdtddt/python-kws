# BeautifulSoup 외부 패키지 설치
# cmd(명령 프롬프트): pip install BeautifulSoup4 / pip install bs4
# pip list

#find() 메소드 사용 - 웹페이지 분석 및 추출

import requests
from bs4 import BeautifulSoup

url="https://www.giantsclub.com/html/?pcode=855"
response=requests.get(url)
html = response.text # 그냥 response는 url의 모든 정보가 다 들어있음. text메서드를 써야 html 정보를 가져올 수 있음
soup = BeautifulSoup(html, 'html.parser')

# find() 조건에 맞는 첫 번째 태그만 반환
# id 요소를 찾을 때는 id 파라미터를 사용

id_element=soup.find(id='skipArea')
print(id_element)
print(id_element.text)
print(response)
print(response.status_code)