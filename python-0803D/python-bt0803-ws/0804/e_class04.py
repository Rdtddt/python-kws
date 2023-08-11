class Candy:
     def set_info(self, shape, color):
          self.shape=shape
          self.color=color

satang=Candy() # 값이 없는 인스턴스를 생성
satang.set_info('circle', 'red') # 값을 저장할 수 있는 메소드를 호출

#생성자를 이용한 인스턴스
#생성자: 인스턴스를 생성할 떄 자동으로 호출되는 특별한 메소드
#생성자 형태: __init__() - 파이썬에서 생성자 이름은 항상 __init__ (미리 기능이 부여된 메소드)
#인스턴스 변수 초기화 용도로 사용

class Candy2():
     def __init__(self, shape, color): #값을 부여하는 방식의 차이
          self.shape = shape
          self.color = color
satang=Candy2('circle', 'blue') # 인스턴스 생성과 동시에 저장 가능
print(satang.shape, satang.color)

#소멸자 #
#: 인스턴스가 소멸될 때 자동으로 호출되는 메소드
#: __del__()

class Sample():
     def __del__(self):
          print('인스턴스가 소멸됩니다.')
sample=Sample()
del sample # del
