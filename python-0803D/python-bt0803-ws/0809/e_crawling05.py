### 네이버 메인 페이지의 전체 소스코드 가져오기
#  requests: 웹페이지의 정보 가져오기
# BeautifulSoup: 원하는 정보만을 가져오기

import requests

url='https://www.naver.com'

# HTTP get 요청을 통해 페이지 정보 가져오기
response=requests.get(url)

# HTTP 응답 상태 코드 출력(200이면 성공)
print("status code: ", response.status_code)

print(response.text[:200])#스플라이싱