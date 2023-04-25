# 파일 입출력
# 파이썬에서 파일 생성, 수정

# open()
# 파이썬 내장 함수
# 파일을 열고, 파일 객체를 리턴한다.
# open(파일 이름(경로), 파일 열기 모드)
f = open("C:/Users/405/my_study/python_study/새파일.txt", 'w')
    # '파이썬 스터디'파일의 경로(절대 경로)안에 새파일.txt를 만듬, 쓰기모드
f.close()
# 오픈했으면 클로즈를 꼭 해야함

# 파일의 경로
# 절대 경로 : C:/ D:/처럼 최상단 경로부터 나타낸 경로(주소)
# 상대 경로 : 현재 작업 위치부터 나타낸 경로

# 파일 열기 모드
# r : 읽기 모드, 파일을 읽기만 할 때 사용 (기존에 파일이 존재해야함. 내용 추가입력 불가)
# w : 쓰기 모드, 파일에 내용을 쓸 때 사용 (파일을 생성하거나 내용을 입력하고싶을때)
# a : 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용 (10번째 줄에 파일을 추가한다던가 등)

# w 쓰기모드
f = open("python_study/새파일.txt", 'w', encoding="utf=8") # 깨짐 방지 인코딩도 함
for i in range(1, 11):
    print(i,"번째 줄")  # TERMINAL에 출력
    f.write(str(i)+"번째 줄\n")  # 괄호 안에 가진 내용을 f 안에(새파일.txt) 출력
f.close()
# w 모드는 덮어쓰기 된다.
# 파일이 없으면 새로 생성함 

# a 추가모드
f = open("python_study/새파일.txt", 'a', encoding="utf=8")
for i in range(11, 21):
    print(i,"번째 줄")  
    f.write(str(i)+"번째 줄\n")
f.close()
# w처럼 덮어쓰기가 아닌 내용을 추가한다. 
# 파일이 없으면 새로 생성함

# r 읽기모드
f = open("python_study/새파일.txt", 'r', encoding="utf=8")
line = f.readline()
print(line)
line = f.readline()
print(line)

while True:
    line = f.readline()
    if line == "":
        break
    print(line)
f.close
# 실행 결과 : 첫번째 줄
#            두번째 줄
# readlien()함수
# 첫번째 줄부터 1줄씩
# 커서가 이동하는 것처럼 읽어옴
# 처음부터 끝까지 읽어오려면 반복문 사용

# readlines() 함수
# 파일의 모든 줄을 읽어서 [리스트]로 반환
f = open("python_study/새파일.txt", 'r', encoding="utf=8")
lines = f.readlines()
print(lines)

lines = f.readlines()
for line in lines:
    print(line)
f.close
# 실행 결과 : ['1번째 줄\n', '2번째 줄\n', ... '20번째 줄\n']
# 한 줄씩 출력하려면 반복문 사용(readlien()함수와 실행 결과가 같음)

# read() 함수
# 파일 내용 전체를 문자열 하나로 리턴한다
f = open("python_study/새파일.txt", 'r', encoding="utf=8")
data = f.read()
print(data)
f.close

# for문으로 읽기
f = open("python_study/새파일.txt", 'r', encoding="utf=8")
for line in f:
    print(line)
f.close

# with문 (고급방식)
# open - close를 자동으로 해줌
with open("python_study/새파일.txt", 'a', encoding="utf=8") as f:
    f.write("end of file")

# csv(comma separated valuse)
# ,로 구분되는 값들을 모아놓은 파일
# 콤마로 표를 만든 것. 띄어쓰기 필요없음
with open("python_study/data.csv", 'w', encoding="utf-8") as f:
    f.write("날짜,날씨,기온\n")
    f.write("20230424,맑음,10\n")
    f.write("20230425,비,9\n")
with open("python_study/data.csv", 'r', encoding="utf-8") as f:
    data = f.readlines()
    print(data)
    

# 계산기 결과 저장 함수
# 정수 2개를 입력받고 두 수를 더한 결과를 
# add_result.txt 파일에 저장하는 함수를 정의하세요
# 함수 이름 : add_write
def add_write(a,b):
    result = a + b
    with open("python_study/add_result.txt", 'w', encoding="utf=8") as f:
        f.write(str(result))
add_write(1, 2)

# 텍스트 파일에 적힌 숫자 2개를 읽어와서 더하는 함수를 정의하세요
# 텍스트 파일 이름 : add_number.txt
# 경로 : python_study/add_number.txt
# 정수 2개를 더한 값을 프린트 하세요
# 함수 이름 : read_add_print
def read_add_print():
    with open("python_study/add_number.txt", 'r', encoding="utf=8") as f:
        data = f.read()
        a = int(data[0])
        b = int(data[2])
        print(a + b)
read_add_print()
