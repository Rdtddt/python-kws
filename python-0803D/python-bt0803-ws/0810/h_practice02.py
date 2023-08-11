import requests
from bs4 import BeautifulSoup

url = 'https://www.cgv.co.kr/'
params = {
     'Napm': ''
}
response=requests.get(url, params=params)
soup = BeautifulSoup(response.text, 'html.parser')

# CGV 영화 예매 사이트 메인 페이지의 무비차트의 영화제목을 가져오기
# class=movieName
class_elements=soup.find_all(class_="moviename")
for element in class_elements:
     print(element)