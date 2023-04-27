# 표준 라이브러리
# 모듈을 모아놓은 것 -> 패키지
# 패키지를 모아놓은 것 -> 라이브러리
# 파이썬에서 지원하는 표준 라이브러리
# 파이썬을 설치할 때 자동으로 함께 설치
# 따로 설치하지 않고 import 명령어로 불러옴

# datetime 라이브러리
# 날짜 관련 라이브러리
# datetime의 date 객체 사용
import datetime
day1 = datetime.date(2023, 4, 17)
day_end = datetime.date(2023, 9, 18)
diff = day_end - day1  # 날짜끼리 뺄셈 가능
print(diff.days)  # 결과: 154

# 2018년 8월 6일은 무슨 요일?
# weekday() --> 0:월요일, 1:화요일 ~~ 6:일요일
import datetime
day = datetime.date(2018, 8, 6)
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
print(day.weekday())  # 결과: 0  
print(weekdays[day.weekday()])  # 결과: 월요일

# datetime의 포멧팅 코드
# 날짜랑 시간을 표시하는 방법
# 년/월/일
# 월/일/년
# 일/월/년
# 2023년 4월 27일
# 2023-04-27
# 23년 4월 27일
import datetime
today = datetime.datetime.today() 
# 현재 컴퓨터 시스템의 날짜와 시간을 가져옴
print(today)  # 결과: 2023-04-27 10:49:16.076617

# strftime()
print(today.strftime("%Y년 %m월 %d일"))  # 결과: 2023년 04월 27일
# %Y 년도 4자리
# %y 년도 2자리
# %m 월
# %d 일
# %H 시간(24시간)
# %I 시간(12시간)
# %M 분
# %S 초
# %A 요일
# !대소문자 구분 주의!
print(today.strftime("%A"))  # 결과: Thursday

# time 라이브러리
# 시간 관련 라이브러리
import time
time_now = time.time()
print(time_now)  # 결과: 1682561127.0543532 (컴퓨터의 시간. 초)
print(time.strftime("%H:%M:%S",time.localtime(time_now)))  # 결과: 11:05:27

# time.sleep()
# 프로그램이 잠깐 멈췄다가 실행하기
import time
print("before")
time.sleep(1) 
print("after")  # 1초 뒤 출력
for i in range(10):
    print(i)
    time.sleep(1.2)  # 0~9까지 1.2초씩 쉬었다가 출력
# 정확하진 않지만 1초와 매우 유사하게 작동함

# math
# 수학 계산 관련
import math
result = math.ceil(1.1) # ceil: 올림하는 함수
print(result)  # 결과: 2
result = math.floor(1.9) # floor: 내림하는 함수
print(result)  # 결과: 1
print(math.pi)  # 결과: 3.141592653589793

# random
# 난수(규칙이 없는 임의의 수) 관련
# 범위 내에서 무작위로 숫자를 출력해줌
import random
random.random()
# 0.0 ~ 1.0 사이의 실수 중 난수 값
random_value = random.random()
print(random_value)  

# random.randint(시작, 끝)
# 시작 ~ 끝 사이의 정수 중 난수 값 
random_value = random.randint(1, 10)
print(random_value)

# random.choice(리스트)
# 리스트의 요소 중 무작위로 하나를 리턴
foods = ["서브웨이", "맥도날드", "짜장면", "국밥", "김치찌개"]
food = random.choice(foods)
print(food)

# random.shuffle(리스트)
# 리스트의 요소 순서를 무작위로 바꿈
# 데이터는 변하지 않음
li = [1, 2, 3, 4, 5]
random.shuffle(li)
print(li)

# 로또번호 출력하기 1
lotto_numbers = list(range(1, 46))  # 1 ~ 45까지의 숫자를 리스트에 넣음
my_lotto = []
for i in range(6):
    random_value = random.choice(lotto_numbers)
    if random_value not in my_lotto:   # 중복 숫자 체크하기
        my_lotto.append(random_value)  # 체크한 뒤에 리스트에 넣음
print(my_lotto)

# in 연산자
# a in b
# a가 b에 포함되어 있으면 True
# a가 b에 포함되어 있지 않으면 False

# not in 연산자
# a not in b
# a가 b에 포함되어 있지 않으면 True
# a가 b에 포함되어 있으면 False

li = [1,2,3,4,5]
a = 10
for i in li:
    if a == i:
        print("있음")
# 위 코드보단 축약된 표현으로 사용 가능하다. for문이 마냥 좋은건 아니라고
if a in li:
    print("있음")

# 로또번호 출력하기 2
lotto_numbers = list(range(1, 46))
random.shuffle(lotto_numbers)
my_lotto = lotto_numbers[:6]
print(my_lotto)


# 색 이름과 음식 이름을 합치면 멋진 밴드 이름이 된다고 합니다.
# 색 이름과 음식 이름을 무작위로 뽑아 밴드 이름을 추천하는 프로그램을 만들어보세요.
import random
colors = ["베이지","블랙","블루","회색","청색","레드","파란","핑크","그린"]
foods = ["쭈꾸미","요거트","오란다","와플","아이스티","떡볶이","커피","고구마"]
color = random.choice(colors)
food = random.choice(foods)
print(color + food)  # print(f"{color} {food}")


# 삼항 연산자
# 연산자가 항을 세개 갖는다
# 참일때값 if 조건(참,거짓) else 거짓일때값
# if문이랑 생김새는 달라도 기능은 같음 
result = "참" if True else "거짓"
result = "참" if False else "거짓"
print(result)

def is_odd_number(n):
    return "홀수" if n % 2 == 1 else "짝수"
    # 한 줄로 코드를 짤 수 있다


# 숫자야구 게임
# 1. 정답을 정한다. 정답은 4자리 숫자(랜덤)
# 2. 게임 유저가 정답을 입력한다.
# 3. 정답과 비교해서 S / B / OUT 개수를 알려준다.
# 4. 정답을 맞추거나, 종료를 입력하면 끝낸다.
# 5. 정답을 맞췄을 때 "한번 더 하시겠습니까?" 라고 물어보게 한다.
import random
numbers = list(range(10))
random.shuffle(numbers)
answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]  # 삼향연산자
while True:
    user_input = input("정답은? ")
    if user_input == "종료":
        print("종료되었습니다.")
        break
    # 4자리 수는 입력했는데 만약 공백이 같이 입력되면 --> isdigit()에서 걸러짐
    # 또는 미리 제거해준다 --> stip()함수 사용
    user_input = user_input.strip()

    # 만약 숫자가 아닌 값이 입력된다면 다시 입력하게 한다. --> 처음으로 간다 --> continue 사용
    # isdigit() : 숫자로만 이루어진 문자열인지 확인함. 맞다면 Ture, 아니면 False
    if not user_input.isdigit():
        print("4자리 숫자만 입력하세요.")
        continue

    # 만약 4자리 숫자가 아니라면 다시 입력하게 한다. --> 처음으로 간다 --> continue 사용
    elif len(user_input) != 4:
        print("4자리 숫자를 입력하세요.")
        continue
    # 첫 글자가 0인 경우 --> continue
    elif user_input[0] == '0':
        print("첫 숫자는 0이 아닌 다른 숫자 4자리로 입력하세요.")
        continue

    # 숫자 중복 확인
    duplicate = False
    for i in range(3):
        if user_input[i] in user_input[i+1:]:
            duplicate = True
            break
    if duplicate:
        print("숫자 중복이 없게 4자리로 입력해주세요.")
        continue
    
    # 게임 돌아가는 구간
    strike = 0
    ball = 0
    out = 0
    for i in range(4):
        input_value = int(user_input[i])
        if input_value not in answer:
            out += 1
        elif input_value == answer[i]:
            strike += 1
        else:
            ball += 1
     
    print(f"strike: {strike}, ball: {ball}, out: {out}")

    # 게임 끝나는 구간
    if strike == 4:
        print("정답!")
        user_input = input("한번 더 하시겠습니까?[y/n] > ") 
        if user_input == "y":  # 'y'를 입력하면 다시 문제 주어지고 처음으로
            numbers = list(range(10))
            random.shuffle(numbers)
            answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
        else:
            print("종료되었습니다.")
            break
            

# os 라이브러리
# OS(운영체제) 자원을 제어
import os

# os.environ
# 시스템의 환경 변수 값을 리턴한다.
print(os.environ)

# os.getcwd()
# get current working directory
# 현재 작업 공간(파일 이름)을 절대 경로로 리턴한다.
print(os.getcwd())

# os.mkdir(디렉터리)
# 현재 작업 공간에 디렉토리(폴더)를 만든다.
os.mkdir("폴더1")

# os.rename(원래이름, 바꿀이름)
# 파일의 이름을 바꾼다.
os.rename("파일1", "파일2")

# os.rmdir(디렉터리)
# 디렉토리(폴더)를 지운다.
# 폴더 안에 아무것도 없어야 된다. (비어있어야 함)
os.rmdir("폴더1")

# os.unlink(파일)
# 파일을 지운다. 
os.unlink("파일2")

# os.path
# os.parh.exists("경로")
# 파일이 있으면 True, 없으면 False
import os
if os.path.exists("없는파일"):
    f = open("없는파일",'r')
else:
    print("파일이 없습니다.")
# 2
if not os.path.exists("없는파일"):
    f = open("없는파일",'w')
    f.close
f = open("없는파일",'r')

# os.path.join("경로","경로","경로")
# 경로를 합쳐서 1개의 경로로 만들어준다.
import os
cwd = os.getcwd()
my_folder = "python_study"
file_name = "test_file.txt"
file_path = os.path.join(cwd, my_folder, file_name)
with open(file_path, "w", encoding="utf-8") as f:
    f.write("테스트 파일을 작성합니다.")


# 외부 라이브러리
# 파이썬 표준 라이브러리가 아닌 라이브러리
# pip를 사용해서 설치한다.

# pip
# package installer for python
# 파이썬 모듈, 패키지 설치하는 도구
# PyPI(파이썬 패키지 인덱스) 파이썬 소프트웨어 저장 공간
# PyPI에 있는 파이썬 패키지를 설치해준다.
# TERMLNAL에서 입력

# 패키지 설치(최신 버전)
# pip install 패키지이름

# 패키지 삭제
# pip unistall 패키지이름

# 특정 버전으로도 설치 가능
# pip install 패키지이름==1.0.5

# 최신 버전으로 업그레이드
# pip install --upgrade 패키지이름

# 설치된 패키지 리스트 확인
# pip list
