#이름, 학년, 반
#이승아, 1학년, 3반
#이준국, 2학년, 8반

#1. CSV 파일 읽기
# - 한 줄에 한 데이터: realine() 메소드로 한 줄씩 읽기
# - 쉼표로 분리: split() 메소드로 분리



student_list=[]
with open('D:\\0803D\\python-bt0803-ws\\0803\\File_IO\\student.scv', 'rt', encoding='utf-8') as file:
    file.readline()
    while True:
        line=file.readline()
        if not line:
            break
        student=line.split(',')
        student_list.append(student)
print(student_list)

#2. csv 모듈 사용
#csv 모듈로 csv 파일 읽기
#csv.reader() 메소드는 csv 파일의 내용을 일고 그 내용을 저장한 객체를 반환
import csv
with open ('D:\\0803D\\python-bt0803-ws\\0803\\File_IO\\student.scv', 'rt', encoding='utf-8') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#csv 모듈로 csv 파일 생성
#csv.writer 객체를 이용하여 csv 파일 작성 가능


header = ['이름', '나이', '직업']
data = [['이승아', 50, 'Developer'], ['이준국', 60, 'doctor']]

with open('person.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(header)
    writer.writerows(data)