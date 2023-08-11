## 검색결과 웹페이지 정보 가져오기 예제 실습

# 롯데 자이언츠 경기일정 페이지의 정보를 가져오는
# 파이썬 웹 크롤링 코드 작성
# url 파라미터 설정을 params,
# 롯데 자이언츠 기본 URL: base_rul

# https://www.giantsclub.com/html/?pcode=257

import requests

# 롯데자이언츠 기본 URL
base_url = "https://www.giantsclub.com/html/"

# URL 파라미터 설정
parameter={"pcode": "257"}

# User-Agent 설정(웹 서버에서의 차단을 피하기 위해 설정): headers
user_agent = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response=requests.get(base_url, params=parameter, headers=user_agent)

# 웹 페이지가 정상적으로 응답을 반환했는지 확인
if response.status_code ==200:
     print(response.text)
else:
     print(f'Error {response.status_code}: Unable to fetch the webpage')

#