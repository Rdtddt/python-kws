class Book:
     title='' # 없어도 됨
     author=''
     def set_info(self, title, author):
          self.title=title
          self.author=author
     def print_info(self):
          print("제목은 {}, 저자는 {}입니다.".format(self.title, self.author))


book1=Book()
book2=Book()
book1.set_info('파이썬', '개발자')
book2.set_info('어린왕자', '생택쥐페리')

book_list=[book1, book2]

for book in book_list:
     book.print_info()

#! self 키워드
# 클래스 내부에서 호출한 객체를 찾기 위해 해당 함수를 호출한 객체를 가리킴