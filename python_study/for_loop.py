# for 반복문
"""
for 변수 in iterable(데이터 세트)값:
    반복할 코드
"""
li_1 = ["one","two","three"]
for i in li_1:
    print(i)
# 첫번째 요소부터 마지막 요소까지 변수(i)에 하나씩 대입해서 반복 출력
s1 = "hello"
for i in s1:
    print(i)
# 첫번째 글자부터 마지막 글자까지 변수(i)에 하나씩 대입해서 반복 출력
# while 처럼 무한반복은 불가능
# 반복 횟수가 정해져 있을때 사용하기 좋음

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(i)
numbers.reverse()  # 순서 뒤집기
for i in numbers:
    print(i)

# range()
# 리스트를 만들지 않고 숫자 range(범위. 데이터 갯수) 객체를 만들어주는 함수
# range(끝 정수)
# 0 ~ 끝 정수-1
for i in range(10):
    print(i)  # 결과 0 ~ 9 

# range(시작, 끝)
# 시작 ~ 끝 정수-1
for i in range(1, 11):
    print(i)  # 결과 1 ~ 10

# range(시작, 끝, 스텝)
# 시작 ~ 끝 정수-1 까지인데 스텝만큼 차이나게
for i in range(1, 21, 2):
    print(i)  # 결과 1 ~ 19 까지 2씩 차이나게

#for문을 사용하여 2부터 30까지 출력해보세요
for i in range(2, 31):
    print(i)

# for문을 사용하여 2부터 30까지 숫자 중 짝수만 출력해보세요
# 방법 1
for i in range(2, 31, 2):  # 2 ~ 30까지 2씩 차이나게
    print(i)
# 방법 2
for i in range(2, 31):
    if i % 2 == 1:  # 홀수
       pass # 아무것도 안하고 건너뜀. continue와는 다름
    else:   # 짝수
        print(i)
# 방법 3
for i in range(2, 31):
    if i % 2 == 0:  # 짝수
        print(i)

# for문을 사용하여 10부터 1까지 출력해보세요
# 방법 1
for i in range(10, 0, -1):  # 10부터 0까지 -1씩 차이나게 
    print(i)
# 방법 2
for i in reversed(range(1, 11)): 
    print(i)
# 방법 3
for i in range(1, 10)[::1]:  # 슬라이싱. [시작인덱스 : 끝인덱스 : 방향(음수면 뒤집어서)] < 보통은 이렇게 잘 안쓴다는?
    print(i)


money = 2000
price = 1000
coffee = 5
# 방법 1
for i in range(coffee):  # 0 ~ 4
    print("커피를 구매했습니다.")
    money -= price
    print("남은 커피: ", coffee - 1 - i)  # 처음 실행할 때 5-1-0 이여서 결과값은 4 
    if money < price:
        break
# 방법 2
for i in range(1, coffee, +1):  # 1 ~ 5
    print("남은 커피: ", coffee - i)
    if money < price:
        break
#방법 3
for i in range(coffee):  
    coffee -= 1  
    print("남은 커피: ", coffee)  # 4 ~ 0
    if money < price:
        break

prices = [500, 700, 930]
money = int(input("돈:"))
# 방법 1
for i in range(len(prices)):  # 몇번 실행할건지 len함수로 prices리스트의 길이를 구함
    price = prices[i]
    print(money // price)
    print(money % price)
# 방법 2
for price in prices:  
# price = prices[i]처럼 별도의 변수 선언 없이 for문 한 줄로 선언
# 이렇게해도 리스트에서 하나씩 꺼내오고 실행 횟수도 정해짐
    print(money // price)
    print(money % price)

# 리스트에 넣기
scores = []
for i in range(5):  # 5번 넣기로 선언
    scors = int(input("시험점수:"))
    scores.append

# 이중 for문
# 2 ~ 9단 만들기
for i in range(2, 10):  # 2 ~ 9
    print(i, "단")
    for j in range(1, 10):
        print(i, "*", j ,"=", i*j)
    print("-----------")

    