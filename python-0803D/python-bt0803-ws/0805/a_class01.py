##클래스 변수##
# alt shift 방향키 / alt 방향키
#1. 인스턴스
#인스턴스마다 서로 다른 값을 가지는 경우에는 인스턴스 변수를 사용
#모든 인스턴스 변수는 self.xxx fh 로 사용

#2. 클래스 변수
#클래스 내부에서 정의되지만, 메서드 외부에서 선언되는 변수
#해당 클래스의 모든 인스턴스에서 공유되는 값 저장

class Korean:
     country='한국' # 클래스 변수
     def __init__(self, name, age, address):
          self.name=name # 인스턴스 변수
          self.age=age
          self.address=address

man1=Korean('이준국', 29, '부산') #객체
print(man1.name) # 인스턴스 변수는 해당 인스턴스에서 불러오기 가능
print(man1.age)
print(man1.address)
#print(Korean.address) 인스턴스 변수는 인스턴스 접근만 가능

print(man1.country) # 클래스 변수는 인스턴스, 클래스 모두에서 불러오기 가능
print(Korean.country)

class Myclass:
     class_variable='이것은 클래스 변수입니다'

instance1=Myclass()
instance2=Myclass()

print(instance1.class_variable)
print(instance2.class_variable)

Myclass.class_variable="변경된 클래스 변수 값"

print(instance1.class_variable)
print(instance2.class_variable)