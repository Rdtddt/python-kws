#클래스 예제: 계산기
#사용자로부터 수식 입력받고, 입력된 수식의 결과를 출력하는 calculator 클래스

class Calculator:
     def input_expr(self): # 수식을 입력받에서 expr에 저장
          expr = input('수식을 입력하세요 >> ')
          self.expr=expr # 우항의 exper은 이전 줄의 입력값

     def calculate(self):
          #eval(): 문자열로 된 수식 자체를 계산할 수 있는 내장 함수
          return eval(self.expr)

calc=Calculator() #Calculator 클래스의 calc 인스턴스를 생성
calc.input_expr() #콘솔창 생성

print('수식 결과는 {}입니다.'.format(calc.calculate())) #calculate() 메서드를 호출하면 수식 결과가 반환되면서 결과 출력3+5

