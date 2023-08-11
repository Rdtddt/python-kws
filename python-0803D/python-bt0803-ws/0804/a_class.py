### 객체와 클래스
# 객체: 서로 많은 데이터를 하나로 묶어서 표현한 것

#! 클래스
# 클래스: 객체를 만드는 도구

# 와플(객체) 와플머신(클래스)
# 같은 클래스로 나온 객체라 하더라고 객체들은 서로 다른 값을 가질 수 있음

#!인스턴스
#인스턴스: 클래스를 이용해서 생성한 카리키는 용어

# 와플머신 클래스로 만든 와플은 객체(object)
# 와플은 와플머신 클래스로 만든 인스턴스(instance)
# 객체=인스턴스라고 해도 무방

#! 클래스 정의
# : 클래스를 생성
# class 키워드로 클래스를 정의
# 클래스 이름은 upper came1 case 규칙을 따름

#! 명령 규칙
#변수, 함수: snake_case
#클래스는 Upper Camel case

# UpperCamelCase : 첫 글자 & 이어지는 단어의 첫 글자를 대문자로 작성
# MyBestFriend
# LowerCamelCase : 이어지는 단어의 첫 글자만를 대문자로 작성
# myBestFriend

#! 클래스 기본 형식
#class 클래스명:
    #본문 (클래스 상세정의)

#! 객체 생성
#객체명 = 클래스()

#! 클래스 정의와 객체 생성
class WaffleMachine:
    pass # 아무 런 정의 없이 클래스를 생성
waffle = WaffleMachine() # waffle(객체)

print(waffle)
#그러면 이렇게 뜸: <__main__.WaffleMachine object at 0x0000018879420F90>