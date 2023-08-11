### 객체지향 프로그램 도입의 필요성

# 학생 정보를 전달하는 student_into() 함수
# 이름, 학년, 반, 전화번호, 주소, 성적

#학생정보를 print문으로 출력할거임
def student_info(name, grade, class_number, phone_number, address, score):
    print(name)
    print(grade)
    print(class_number)
    print(phone_number)
    print(address)
    print(score)

#student_info() 함수를 사용하여 학생을 생성

name1='Lee Seungah'
grade1 = 3
class_number=2
phone_number="010-1111-2222"
address = "부산시 부산진구"
score = 85
student_info(name1, grade1, class_number, phone_number, address, score)

#student2에 대해서 반복
name1='Lee Seungah'
grade1 = 3
class_number=2
phone_number="010-1111-2222"
address = "부산시 부산진구"
score = 85
student_info(name1, grade1, class_number, phone_number, address, score)

#클래스를 사용한 관리
class Student:
    def __init__(self, name, grade, class_number, phone_number, address, score):
        self.name=name
        self.grade=grade
        self.class_number=class_number
        self.phone_number=phone_number
        self_address=address
        self.score = score

student1 = Student('이승아', 3, 2, '010-1111-2222','부산시', 90)
student2 = Student('이승아', 3, 2, '010-1111-2222','부산시', 77)

print(student1.name)