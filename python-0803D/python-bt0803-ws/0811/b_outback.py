import requests
from bs4 import BeautifulSoup

url="https://www.outback.co.kr/menu/productView.do?cateIdx=49&pdtIdx=10314&menuIdx=43"
response=requests.get(url)
html = response.text
soup=BeautifulSoup(html, 'html.parser')

id_element=soup.find(id='dHead')
print(id_element.text)