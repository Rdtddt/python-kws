###검색결과 웹페이지 정보 가져오기
#https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=파이썬

# 사용자가 서버에게 요청하는 정보들이 전달되는 구역(? 오른쪽)
# 검색어나 다른 조건을 웹 페이지에서 입려하는 경우 URL에 파라미터가 추가됨.
# 해당 파라미터들은 '파라미터명=값'(key=value) 형태로 구성
# 정보가 여러 개인 경우 &를 사용하여 이어서 작성

# 입력한 검색어 '파이썬'은 query라는 파라미터로 전달

import requests

url='https://search.naver.com/search.naver'

# 검색어 파라미터 설정
params = {"query": "파이썬"}

#HTTP 헤더
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

#requests 라이브러리를 사용하여 웹 페이지 정보 가져오기
response = requests.get(url, params=params, headers=headers, timeout=10)

#requests.get() 메소드
#1.url(필수): 가져올 페이지의 url을 문자열로 전달
#2. params: url에 추가할 파라미터를 딕셔너리 형태로 전달
#3. headers: 웹페이지 요청시 함께 전달될 http 헤더를 딕셔너리 형태로 전달
#4. timeout: 요청에 대한 최대 대기 시간을 초 단위로 지정
#  지정한 시간 내에 응답이 오지 않으면 timeout 오류 발생

#가져온 웹페이지 정보 출력
print(f'Status code: {response.status_code}')
print(response.text[:200])

