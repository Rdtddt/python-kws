##1. 클래스 메서드 정의
# @classmathod 데코레이터를 사용하여 정의된 메서드

class Myclass:
     class_var = "클래스 변수"
     
     @classmethod
     def class_method(cls):
          return cls.class_var
     
#2. 클래스 메서드 특징
#2-1. 첫 번째 매개변수로 클래스 객체를 받는다. (cls 이름을 사용)
#인스턴스 객체 없이도 호출 가능
#클래스 메소드는 클래스 이름을 통해 호출 가능(클래스 자체에서 직접 호출 가능)

class Korean:
     country: '한국' #클래스 변수

     @classmethod
     def trip(cls, country): #첫 매개변수는 cls
          if cls.country == country:
               print('국내 여행입니다')
          else:
               print('해외 여행입니다')

Korean.trip('한국')
