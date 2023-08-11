### 강제로 예외발생 시키기
# raise 키워드로 강제로 예외 발생

# raise 예외 클래스()
# raise 예외 클래스('예외 메시지')

age = int(input('나이를 입력하세요: '))

if age < 0:
     raise ValueError('나이는 음수일 수 없습니다.')
print(age)

#! 2. 사용자 예외 클래스
# 파이썬 내장 예외 클래스 외에도 사용자가 직접 예외 클래스를 정의 가능
class HourError(Exception):
     def __init__(self):
          super().__init__('올바른 시간이 아닙니다.')

try:
     hour = int(input('시간을 입력하세요'))
     if(hour < 0 or hour > 23):
          raise HourError
except HourError as message:
     print(message)
