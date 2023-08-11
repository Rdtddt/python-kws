#정적 메소드
# 
#클래스나 인스턴스의 상태를 수정하거나 접근하지 않는 메소드
#클래스나 인스턴스의 정보에 접근하지 않음.

#생성자 메소드: __init__(self) 인스턴스 가져옴
#클래스 메소드: def 메소드명(cls) 클래스 가져옴
#정적 메소드: 필수 매개변수가 없음

#인스턴스 없어도 호출 가능(클래스 이름을 통해서도 호출)
#클래스나 인스턴스의 상태와 무관하게 독립적인 로직을 수행할 때 사용

class Myclass:
     class_var='클래스변수'
     @classmethod
     def class_method(cls):
          return cls.class_var
     
     @staticmethod # Myclass와 무관
     def static_method(param1, param2):
          return param1+param2

print(Myclass.class_method())
print(Myclass.static_method(5, 7))

class Korean:
     country='한국'

     @staticmethod
     def slogan():
          print('Imagine your Korea')

Korean.slogan()
