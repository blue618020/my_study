"""
if 조건: 
     실행하려는 코드 
     코드 2줄
     코드 3줄
코드 4줄
"""
# if문은 들여쓰기(Tap)로 구분한다. 코드블록이라고 함
# bool타입 변수 True(참), False(거짓). 앞에 대문자 유의
# if문은 조건이 True(참)일 때만 안쪽 코드블록을 실행

"""
if 조건: 
    조건이 참일 때 실행하려는 코드
else: 
    아닐때 실행하는 코드 
"""
# else는 조건이 False(거짓)일 때만 안쪽 코드블록을 실행

"""
if 조건1:
    조건1이 참일 때 실행
elif 조건2:
    조건1은 거짓, 조건2는 참일 때 실행
else:
    조건 1이 거짓, 조건2도 거짓일 때 실행
"""
# elif는 if 조건의 또다른 선택지를 만듬

number1 = 6
number2 = 6
if number1 > number2:
    print(number1 > number2)
    print("number1이 더 크다.")
elif number1 == number2:
    print(number1 == number2)
    print("같다")
else:
    print(number1 > number2)
    print("number2가 더 크다.")

# 비교 연산자
# a > b   a가 b보다 크다
# a >= b  a가 b보다 크거나 같다
# a < b   a가 b보다 작다
# a <= b  a가 b보다 작거나 같다
# a == b  a와 b가 같다
# a != b  a와 b가 같지 않다
   
print(2 > 3) # False
print(2 >= 3) # False
print(2 < 3) # True
print(2 <= 3) # True
print(2 == 3) # False
print(2 != 3) # True

# # 문자열 알파벳 비교는 사전에 표기한 순서로 비교함. a에서 뒤로갈수록 크기가 커진다는 느낌
print("a" < "b") # True
print("CAT" < "DOG") # True
print("COW" > "CAT") # True
print("DOG" == "dog") # False
print("DOG" > "dog") # False 대문자가 먼저기 때문에 소문자보다 작음

# 논리 연산자 (또는 bool타입 연산자)
# and  a and b. a와 b가 모두 True일 때만 True 아니면 False
# or   a or b. a와 b중 하나가 True면 True 아니면 False
# not  not a. a가 True면 False로, False면 True로 반전시킴

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True

age = 17
money = 10000
if age >= 20 and money >= 10000:
    print("성인이고 부자입니다.")
if age >= 20 or money >= 10000:
    print("성인 또는 부자입니다.")

if "안녕": # 문자열에 값이 있어서 Ture
    print("안녕하세요")

if 0: # 숫자에 값이 없으니 False
    print(0)
