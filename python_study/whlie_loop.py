# whlie 반복문
"""
whlie(~하는 동안)
Whlie 조건:
    반복할 코드
"""
# 조건이 Ture일 경우에 코드를 계속 반복
# 특정 조건 또는 시점에 충족할 때까지 반복할 때 사용하기 좋음 
n = 1 
while n <= 100:
    print(n)
    n += 1 

# += 연산자
# 대입 연산자의 일종
# 더하기 연산 후 할당
# n += 1 은 n = n + 1 라는 의미
# 산술연산자 다 가능
# -=
# *=
# /=
# **=
# //=
# %=
s1 = "안녕"
s1 += "하세요"
print(s1) # 문자열에도 적용 가능

# # while 반복문을 활용하여 10부터 1까지 출력하세요
n = 10
while n >= 1:  # while n > 0: 도 결과가 같아서 가능
    print(n)
    n -= 1

# break
# 반복문을 즉시 종료함
# if문으로 종료 조건을 걸어서 같이 사용함
money = 10000
price = 1000
coffee = 5
while money >= price:
# while money - price >= 0: 도 가능 
    print("커피를 구매했습니다.")
    money -= price
    coffee -= 1
    print("남은 커피:", coffee)
    if coffee == 0:
        break 

count = 1
while count < 4:
    print(str(count) + "!")  # 문자열 연산자를 사용하기 위해 count의 타입을 str로 변경해줌
    count += 1

# while 반복문을 활용하여 1부터 10까지 홀수만 출력하세요
a = 1
while a <= 10:
    if a % 2 == 1:  # if를 사용해서 추가 조건을 걸 수 있음
        print(a)
    a += 1

# continue
# while 반복문의 제일 처음으로 돌아감
b = 0
while b < 10:
    b += 1 
    if b % 2 == 0:
        continue  # 짝수가 나오면 처음으로 돌아가도록
    print(b)

# 무한 반복문 (또는 무한 루트)
# 무한 루트
# 조건식에 True를 입력해 항상 참이 되도록 하여 무한히 반복하게 함
# TERMINAL안에 커서를 놓고 Ctrl + c로 강제 종료 가능
"""while True:
    print("hi")
"""
## 사용자 지정에 따라 강제 종료 버튼을 설정 가능
while True:
    user_input = input("종료하려면 1을 입력해주세요: ")
    if user_input == "1":
        break

# 무한반복문으로 계산기 만들기
# +, -, *, / 계산
# 계산할 타입과 2개의 수를 입력받고 계산 결과 출력하기
# q를 입력하면 종료되도록 하기
print("""
       계산기
    ============
    1. 더하기(+)
    2. 빼기(-)
    3. 곱하기(*)
    4. 나누기(/)
    """)
while True:
    operator = input("계산을 선택하세요: ")
    a = int(input("수 입력: "))
    b = int(input("수 입력: ")) 
    if operator == "1":
        print(a, "+", b,"=", a + b)

    if operator == "2":
        print(a, "-", b,"=",a - b)

    if operator == "3":
        print(a, "*", b,"=",a * b)

    if operator == "4":
        print(a, "/", b,"=",a / b)

    if operator == "q":
        break

# 사용자가 가지고 있는 돈을 입력받기
# 구매할 수 있는 커피의 개수와 잔돈을 출력
# 구매할 수 있는 음료수의 개수와 잔돈을 출력 
# 구매할 수 있는 콜라의 개수와 잔돈을 출력 
# 커피는 500원, 음료수는 700원, 콜라는 930원
# 물품의 개수는 무한하다고 가정
# while 반복문을 사용하여 작성
idx = 0
prices = [500, 700, 930]
money = int(input("돈: "))
while idx < len(prices) :  # prices 리스트 안에 있는 길이만큼 반복 (3번)
    price = prices[idx]  
    print(money // price)
    print(money % price)
    idx += 1
    # price 변수에 리스트에 있는 가격을 할당 (idx가 0이니 prices[0]이 되는거고 1씩 증가)

# while 반복문을 사용해서 
# scores 리스트에 시험 점수 5개를 정수형으로 입력받으세요
idx = 0
scorse = []
while idx < 5:
    sco = int(input("점수: "))
    scorse.append(sco)  # 입력받은 sco(점수)를 append 함수를 사용해서 scorse 리스트에 넣음
    idx += 1            # 이걸 5번 반복
print(scorse)  # 확인할려고 출력함

# while 반복문을 사용해서 
# 구구단 2단을 출력하세요
n = 1
while n < 10:
    print("2 *", n, "=", n * 2)
    n += 1
