## 클래스의 구성
# 사람 : 이름, 나이, 연락처, 주소, ... \ 잔다, 먹는다, 공부한다, 걷는다  ...

#? 클래스 구성 변수:
# 클래스 변수(모든 인스턴스가 공통된 값 공유) & 인스턴스 변수

#? 클래스를 구성하는 함수: 메서드(method)
#: 클래스 메서드, 정적 메서드, 인스턴스 메서드...

#! 2-1 인스턴스 변수:
# 클래스를 기반으로 만들어지는 모든 인스턴스(객체)들이 각각 따로 저장하는 변수
# 클래스 내에서 정의되지만, 각 클래스 인스턴스에서 개별적으로 가지는 변수
# 각 객체의 상태 저장
# self.variable_name

#! 인스턴스 메서드
# 클래스 내에서 정의된 함수, 객체가 수행할 수 있는 동작을 나타냄
# 인스턴스 변수를 사용
# 첫 번째 인자로'self' 를 받아야 함.
# self: 메서드를 호출하는 객체 자신을 참조

class Person:
     def who_am_i(self, name, age, tel, address):
          #self.name은 인스턴스 변수 name을 의미
          #우항의 name은 매개변수 name
          #who
          self.name=name
          self.age =age # seungah.age 에 50을 할당
          self.tel =tel
          self.address =address

seungah = Person()  #객체1
seungah.who_am_i('seungah', 50, '010-1111-2222', ' 부산시')
print(seungah.tel)
print(seungah.address)

jungook = Person()  #객체2
jungook.who_am_i('jungook', 40, '010-3333-4444', '양산시')

print(jungook.name)
print(jungook.age)