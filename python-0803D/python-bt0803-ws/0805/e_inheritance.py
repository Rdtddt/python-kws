# 상속
#1. 정의
# 한 클래스의 속성/메소드를 다른 클래스에 전달
#추가적인 속성이나 메소드를 정의할 수 있다.

# 부모 클래스(슈퍼 클래스, 상위 클래스): 상속해 주는 클래스
# 자식 클래스(서브 클래스): 상속받는 클래스

#! 필요성:
#재사용성 : 코드 중복 방지
#확장성 : 기본 클래스를 수정하지 않고 새로운 기능을 추가 & 기본 기능 수정 가능
#모듈화 : 특정 기능의 집합을 부모 클래스에서 정의, 여러 자식 클래스를 정의하여 모듈화된 설계 가능

#! 상속 관계 구현
# ~은 ~이다
class Parentclass:
     def method_in_parent(self):
          print('이 메소드는 부모 클래스에서 정의되었습니다')
class Childclass(Parentclass):
     pass #특별한 동작 X

parent = Parentclass()
child = Childclass()

parent.method_in_parent()
child.method_in_parent()
