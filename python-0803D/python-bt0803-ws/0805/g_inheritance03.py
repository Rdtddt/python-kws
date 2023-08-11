### 서브 클래스의 __init__() ###

# 서브 클래스의 생성자를 구현할 때는 반드시 슈퍼 클래스의 생성자를 먼저 호출해야 함
class ParentClass:
     def __init__(self, name):
          self.name=name
          print(f"Parent's __init__ called with name: {self.name}")

class ChildClass(ParentClass):
     def __init__(self, name, age):
          super().__init__(name)
          self.age=age
          print(f"child's __init__ called with name: {self.name} and age: {self.age}")
child=ChildClass('DoKyung', 10)

#서브 클래스의 인스턴스 자료형#
#슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
#서브 클래스의 객체는 서브 클래스의 인스턴스이면서 슈퍼 클래스의 인스턴스

#isinstance(객체, 클래스)
#결과값을 boolean으로 변환

print(isinstance(child, ChildClass)) # True
print(isinstance(child, ParentClass))

#?sdf 
