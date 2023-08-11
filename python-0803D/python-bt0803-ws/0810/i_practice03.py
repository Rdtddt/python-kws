### 네이버 웹툰 실시간 인기웹툰
#pip install lxml
import requests
from bs4 import BeautifulSoup
import csv

url= "https://comic.naver.com/index"

#엑셀 파일로 저장
fileName = 'naver_webtoon.csv'
f=open(fileName, 'w', encoding = 'utf-8', newline="")
writer = csv.writer(f)


#컬럼 속성명
columns_name = ['순위', '웹툰명']

writer.writerow(columns_name)

# 웹 서버에 요청
response=requests.get(url)
response.raise_for_status() # 에러 알려줌

soup=BeautifulSoup(response.text, 'lxml') #html.parser가 너무 큰어 인지 못함
#전체 영역에서 'class_text'를 찾지 않고
# 실시간 인기 웹툰 영역으로 범위 제한
cartoonsBox=soup.find('div', attrs={'class': 'component_wrap'})

# 실시간 인기 웹툰 영역에서 class 명이 text인 값을 모두 가져와서 cartoons 변수에 할당
cartoons= cartoonsBox.find_all(class_='text')

class_elements = soup.find_all(class_='text')
for element in class_elements:
     print(element.text)
     
