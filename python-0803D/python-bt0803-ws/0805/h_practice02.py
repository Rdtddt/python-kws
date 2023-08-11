#
#!
#?
#^
#*
###

#파이썬 클래스 예제#
#가게 매출을 구할 수 있는 shop 클래스 구형
#1. Shop 클래스
# total=0(클래스 변수 - 전체 매출액)
# menu_list=[{'떡볶이: 3000}, {'어묵': 700}]
# (클래스 변수 - {메뉴명: 가격} 딕셔너리)

class Shop:
     total=0 # 클래스 변수
     menu_list = [{'떡볶이': 3000}, {'어묵': 700}, {'튀김': 500}, {'김밥': 2000}]

     @classmethod
     def sales(cls, menu, amount):
          for item in cls.menu_list:
               if menu in item:
                    cls.amount += item[menu]*amount
                    return
               print(f'{menu}는 저희 가게 메뉴에 없습니다.')
          # for in 반복문
          # 메뉴 리스트에서 메뉴를 가지고 와서
          #해당 메뉴가 메뉴 리스트에 있는지 확인
          #있다면 인스턴스의 총 합계를 할당더하기 연산을 통해 구현



#매출이 생기면 아래의 방식으로 메뉴와 판매량을 작성
#sales() 메소드는 클래스 변수 total과 menu_list를 사용해야 하므로 클래스 메소드로 구현
Shop.sales('떡볶이', 1)
Shop.sales('튀김', 5)
Shop.sales('김밥', 2)

#모든 매출을 작성한 뒤,
print('매출:{}원'.format(Shop.total)) #매출 @원
