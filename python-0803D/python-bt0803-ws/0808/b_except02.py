#1. if문(고전적인 예외처리)
# 코드가 길어짐
a = int(input('정수를 입력하세요.'))
b = int(input('정수를 입력하세요.'))
#a/b
if b!=0:
     print('{}/{}={}'.format(a, b, a/b))
else:
     print('0으로 나눌 수 없습니다.')
num1=5; num2=3
print(num1+num2)

#! 예외의 종류
#2-1. 내장 예외의 종류
# BaseException: 최상위 예외 클래스
# ValueError: 잘못된 값
# TypeError: 잘못된 타입의 데이터 연산
# SyntaxError: 문법이 틀렸을 경우