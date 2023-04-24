# function 함수
# 입력 -> 처리 -> 출력
# input(입력)을 받아서 특정 작업을 수행하고 output(출력)을 반환함

# 내장 함수(built-in)
# 파이썬이 기본적으로 제공해주는 함수
# print()
# len()
# zip()
# int()
# float()
# str()
# list()
# range()

# abs(값)
# absolute(앱솔루트)의 약자
# 입력한 숫자형 데이터의 절댓값(양수)을 반환함
print(abs(100))   # 100
print(abs(-100))  # 100
print(abs(3.15))  # 3.15
print(abs(-3.15)) # 3.15

# sum(리스트)
# 리스트 안의 숫자를 모두 더한 값을 반환함
print(sum([1, 2, 3, 4, 5]))  # 15

# max(리스트)
# 리스트 안에서 최댓값을 찾아 반환함 
print(max([1, 2, 3, 4, 5]))  # 5

# min(리스트)
# 리스트 안에서 최솟값을 찾아 반환함 
print(min([1, 2, 3, 4, 5]))  # 1

# chr()
# 정수 1개를 입력받고 해당하는 유니코드를 반환함 
# ord()와 세트
print(chr(65))  # A

# ord()
# 문자 1개를 입력받고 해당하는 정수를 반환함
# chr()와 세트
print(ord('A')) # 65

# round(값)
# round(값, 소수 자릿수)
# 반올림 함수
print(round(1.234))    # 1
print(round(1.234, 2)) # 1.23
print(round(1.369, 1)) # 1.4


# 함수 정의(define)
# 함수 이름
# 함수 입력값 parameter
# 함수 결괏값 return value
"""
def 함수 이름(함수 입력값):
    함수 기능코드
    return(출력) 함수 결괏값
"""
# def는 함수를 정의하는 명령어
# 함수 이름도 변수 이름의 규칙처럼 지어야 함
# 무슨기능하는지 직관적으로 알아볼 수 있도록 지어야 함
# 영어, 숫자, 언더바(_)만 사용
# 숫자로 시작하면 안됨
# 띄어쓰기 대신 언더바 사용
# 키워드 사용하면 안됨
# 기존에 이미 정의 되어있는 함수 이름은 피하는게 좋음

def print_names():  # 괄호 안을 비워두는건 입력값이 없다는 뜻
    print("손흥민")
    print("황희찬")
    print("김민재")
    print("이강인")  # return이 없는 함수
print_names()  

def get_name():
    return "본인 이름"   # 본인이름을 return하는 함수. 
def print_my_name():
    print(get_name()) # 본인이름을 출력하는 함수

print_my_name()
a = print_names(10)  # 리턴이 없음
b = get_name(10)  # 리턴이 있음
print(a)  # 결과 None
print(b)  # 결과 본인 이름

# return은 있어도 되고 없어도 됨
# 차이점은 없으면 함수로부터 나오는 값이 없음. 출력 수행만 주루룩
# 있으면 함수에 반환해서 나오는 값이 있음. 어떤 변수가 있을때 담아서 사용할 수 있다고

# 입력값 = parameter(파라미터) = 매개변수 = argument(아구미트) 
# '함수에 입력하는 값'이라는 의미에 여러 용어가 있지만 다 같은 말임
def add(a, b):
    return a + b

def print_add(a, b):
    print(a + b)

result = add(1, 2)
print(result)  
# 만든 함수의 출력 결과를 result 변수에 담아서 출력 3
# 요 변수를 사용해서 다른 작업도 수행할 수 있음

result = print_add(1, 2)
print(result)  
# 함수 수행은 되지만 return이 없기 때문에 result변수에 담아서 출력되지 않음(None)
# 그래서 리턴값이 없는 함수는 변수에 담아서 사용하지않음
# print_add(1, 2) 이렇게 호출만 하는 식으로 사용.. 3이 나옴

print_add("안녕","하세요")
# 문자도 호출 가능
print_add(b = "하세요", a = "안녕")
# 이렇게 할당해서도 가능함

def swap_number(a, b):
    temp = a
    a = b
    b = temp  # 두개의 값을 바꿈. 또는 a, b = b, a 도 가능
    print(a, b)
    # return a, b  
swap_number(1, 2)  # 결과 2 1

a = 1
b = 2
print("함수 호출 전", a, b)  # 결과 1 2
swap_number(a, b)   # 결과 2 1
print("함수 호출 후", a, b)  # 결과 1 2
# 함수 안에서 쓰는 a, b와 바깥에서 쓰는 a, b와는 결과가 다름
# 이름만 같고 다른 변수를 가리키기 때문 (이것을 지역변수라고 한다)

a, b = swap_number(a, b)   # 결과 2 1
print("함수 호출 후", a, b)  # 결과 2 1 
# 함수 안에 리턴을 넣고 이렇게 사용하면 호출 후에도 같은 값이 나올 수 있게됨


# 다음 함수를 정의하세요.
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수 2개의 곱
# 내 풀이
def mul(a, b):
    print(a * b)
mul(2, 3)

# 선생님 풀이
def mul(n1, n2):
    return n1 * n2
print(mul(2, 3))
# 위랑 밑이랑 같음
result = mul(2, 3)
print(mul(2, 3))

# 함수 기본값 매개변수
# default value parameter
# 함수 호출 시 n2에 입력된 값이 없으면 기본 값 사용
def mul(n1, n2= 1):
    return n1 * n2
mul(1, 2)  # 결과 2
mul(1)  # b의 기본값인 1이 사용되면서 결과 1

def test_func(x, test= []):
    test.append(x)
    print(x, test)
test_func(1)  # 결과 1 [1]
test_func(2)  # 결과 2 [1, 2]. 누적되기 때문에 기본값을 사용할 때 리스트를 사용하지 말 것

def test_func1(x, test= 5):
    test = test
    print(x, test)
test_func1(1)  # 결과 1, 5
test_func1(2)  # 결과 2, 5. 기본값이 정수이기 때문에 누적되지 않음

def test_func2(x, test= None):
    if test == None:
        test = []   # 리스트를 꼭 사용하고 싶다면 if문으로 체크해서 빈 리스트를 새로 만들게 하면 됨
    test.append(x)
    print(x, test)

# 기본값이 있는 매개변수는 기본값이 없는 매개변수 뒤에 위치해야 함
# 굳이 가운데에 있는 기본값에 매개변수를 주고싶다면 위치를 변경하기 (n1, n3, n2=0)
def sub(n1, n2, n3=0):  
    print(n1 - n2 - n3)

# *args를 사용한 매개변수
# 입력값이 몇개가 될지 모를 때나 안 정해졌을 때 사용
def add_many(*args):
    # 튜플처럼 사용
    # 인덱싱, 슬라이싱 가능
    result = 0
    for i in args:
        result += i
    return result 
result1 = add_many(1, 2, 3, 4, 5)
print(result1)
result2 = add_many(3, 2, 5, 9, 1)
print(result2)
result3 = add_many(1, 2)
print(result3)

# 일반 매개변수와도 같이 사용 가능. 순서를 바꿔도 가능
def calc_many(n1, *args):  
    result = n1
    for i in args:
        result += i
    return n1

# 키워드 매개변수
# **kwargs
# keyword arguments의 줄임말
# 딕셔너리로 사용
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a= 1, b= 1) 
print_kwargs(name= '이름', age= 10)
# 결과 {'a': 1, 'b': 1} 
#      {'name': '이름', 'age': 10}
# 뒤에 있는 값들이 굉장히 유동적일 때 사용함

# 함수 반환
# return 반환값
# return을 만나면 반환값을 반환함과 동시에 함수가 종료됨
def test_5():
    print(1)
    print(2)
    return None
    print(3)
    print(4)
    print(5)
    
# 함수의 반환값은 무조건 1개이다
def test_6(a, b):
    return a + b, a * b
    # return (a + b, a * b)와 같음
result = test_6(1, 2)
res_add, res_mul = test_6(1, 2)  # res_add, res_mul = (a+b, a*b)
print(result)    # 값 (3, 2)
print(res_add, res_mul)  # 값 3 2


# 홀수 판별 함수
# 정수 1개를 입력받고 홀수인지 판별하는 함수 
# 함수 이름 : is_odd_number
# 파라미터 : n
# 반환값 : 홀수면 Ture 짝수면 False
# 내 풀이
def is_odd_number(n):
    if n % 2 == 1:
        print("True")  # 문자열 타입으로 "True"를 출력한 것. 
    else:
        print("False")
is_odd_number(5)

# 방법 1
def is_odd_number(n):
    if n % 2 == 1:
        return True   # bool 타입으로 True를 반환한 것. 이쪽이 문제가 의도한 답이 맞다고 
    else:
        return False
print(is_odd_number(5)) 

# 방법 2 (if문이 많이 중첩되었을 때 유용한 방법)
def is_odd_number(n):
    if n % 2 == 1:
        return True  # 홀수면 안으로 들어가서 종료
    return False     # 짝수면 밖으로 나와서 종료

# 방법 2 (더 짧은 방법)
def is_odd_number(n):
    return n % 2 == 1  # 조건을 계산한 다음에 Ture면 바로 종료


# 테두리를 출력하는 함수
# 문자열을 입력받고 print 함수를 이용해 문자열 길이에 맞게 테두리(*)와 함께 문자를 출력한다.
# 함수 이름 : get_bordered_str
# 파라미터 : message
# 반환값 : Nome (return 없어도 됨)
# print 예시
"""
*****
hello
*****
"""
def get_bordered_str(message):
    message = str(message)  # 12345는 숫자형이기 때문에 문자형으로 변경해주는 단계
    n = len(message)
    print("*" * n)
    print(message)
    print("*" * n)
get_bordered_str("hello")
get_bordered_str(12345)  
# 이렇게 간단한 방법이.. 너무 반복문에 집착했을지도(애초에 세로로 별 5개 찍히기만 했움)


# 속도를 변환하는 함수
# m/s(초당 몇미터)단위의 속도가 입력되면 km/h(시간당 몇키로)단위의 속도로 변환한다.
# 함수 이름 : convert_velocity
# 파라미터 : velocity
# 반환값 : km/h로 변환된 속도
def convert_velocity(velocity):
    # 1초에 1m -> 1m/s
    # 1m/s로 1시간동안 가면 몇 m?
    # 1m/s * 3600(1시간) ==> 3600m/h
    # 1km는 1000m
    # 3600m/h는 몇 km?
    # 3600m/h / 1000(1km)
    # 1m/s * 3600 / 1000 ==> 3.6km/h
    # 초속 * 3600 / 1000 ==> 시속
    # 초속 * 3.6 ==> 시속 
    result = velocity * 3.6
    return result
print(convert_velocity(10))

"""
출력결과 
n = 1
*
n = 4
*
**
***
****
"""
# 별 찍기 함수
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 출력한다
# 함수 이름 : print_stars
# 파라미터 : n
# 반환값 : None
# 내 풀이
def print_stars(n):
    for i in range(1, n + 1):
        print("*" * i)
print_stars(4)

# 선생님 풀이
def print_stars(n):
    for i in range(n):  # 0 ~ n-1
        for j in range(i+1):  # 0 ~ i
            print("*",end="")
        print()
    
    # 풀이 2 while문으로
    i = 0
    while i < n:
        j = 0
        while j < i:
            print("*", end="")
            j += 1
        print("")
        i += 1
print_stars(4)

