## 네이버 뉴스 헤드라인 크롤링 ###
import requests
from bs4 import BeautifulSoup

url="https://n.news.naver.com/mnews/article/029/0002818930?%EB%83%A5=105"
response=requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')

headline = soup('.media_end_head_headline') # 해당 태그 자체 하나를 가져옴
print(headline)