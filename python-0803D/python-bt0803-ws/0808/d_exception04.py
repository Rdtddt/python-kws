### else문과 finally문
#else문: 예외가 발생하지 않으면 처리되는 구문
# finally: 예외 발생과 상관없이 항상 처리되는 구문

#try:
# 코드 작성
#except:
#    예외 발생
#else:
#    예외 없을 때
#finally:
#    언제나 실행되는 영역

try:
     number = int(input('정수를 입력하세요: '))
except ValueError as e:
     print(e)
else:
     print(f'입력한 숫자는 {number} 입니다.')
finally:
     print('프로그램을 종료합니다.')

# finally 문 예제
