#! 1. 모든 예외를 처리하는 방식
# try-except
# 모든 예외를 처리하면 예상치 못한 오류가 발생할 때도 프로그램이 계속될 수 있다.
# 가능한 특정 예외를 지정하여 처리하는 것을 권장
##try:
##     a=int(input('정수를 입력하세요: '))
##     a=int(input('정수를 입력하세요: '))
##     print('{}/{}={}'.format(a, b, a/b))
##except:
##     print('예외가 발생했습니다.')

# 2. 특정 예외만 처리하는 방식
try:
     a=int(input('정수를 입력하세요: '))
     b=int(input('정수를 입력하세요: '))
     print('{}/{}={}'.format(a, b, a/b))
except ZeroDivisionError as e1:
     print(e1)
     print('0으로 나눌 수 없습니다.')
except ValueError:
     print('정수만 입력할 수 있습니다.')
except Exception: 
     print('기타 오류가 발생했습니다.') # 예상치 못한 예외들도 모두 처리하는 구문

# 모든 예외는 기본적으로 예외 메시지를 내장하고 있다.