def swap_value(x, y):
    temp = x
    x = y
    y = temp

def swap_offset(offset_x, offset_y):
    temp = a[offset_x]
    a[offset_x] = a[offset_y]
    a[offset_y] = temp

def swap_reference(list, offset_x, offset_y):
    temp = list[offset_x]
    list[offset_x] = list[offset_y]
    list[offset_y] = temp

a = [1,2,3,4,5]
swap_value(a[1],a[2])
print(a)  # swap 발생X

swap_offset(1,2)
print(a)  # swap 발생O

swap_reference(a, 1, 2)
print(a)  # swap 발생X


# 함수만들기1 - 작은 수를 큰 수로 나눈 몫과 나머지를 반환하는 함수
# 반환 값은 튜플로 되어있으며 몫, 나머지 순으로 되어있다
# 단, 0으로 나누는 것은 불가하기 때문에 두 수 중에 작은 수가 0이라면 
# 화면에 '0은 사용할 수 없습니다.'를 출력하고 종료하기
def div2(a, b):
    if a == 0 or b == 0:
        return ("0은 사용할 수 없습니다.")
    elif a > b:
        c = a // b
        d = a % b
        return (c, d)
    elif a < b:
        c = b // a
        d = b % a
        return (c, d)  
print(div2(10, 1))


# # 선생님 풀이 (모든 상황에 대처하기 위해 짠 느낌)
def div3(a, b):
    if a < b:
        big = b
        small = a
    elif b <= a:
        big = a
        small = b
    else:
        print("정수가 아닙니다.") # 밑에서 걸릴꺼라 없어도 된대
    if small == 0:
        print("0은 사용할 수 없습니다.")
    elif abs(big) < 0 or abs(small) < 0:  # abs(정수 절댓값 연산)
        print("정수를 입력해주세요")
    else:
        q = big // small
        r = big % small
        return (q, r)
print(div3(10, 1))


# 어떠한 string을 받으면 일정한 단위로 끊어서 화면에 출력하는 함수를 짜기
# 끊는 단위는 따로 정하지 않으면 2로 설정
def func(string, unit = 2):
    i = 0
    while i < len(string):
        print(string[i:i+unit])
        i += unit
func("테스트를 위한 문장입니다.")


def test(*args):
    print(args)
test(1,2)  # 결과: (1, 2) 튜플로밖에 안 받아짐

def test2(**kwargs):
    print(kwargs)
test2(a=1,b=2,c=3)  # 결과: {'a': 1, 'b': 2, 'c': 3}


def add_all(*args):
    n = 0
    for i in args:
        for j in i:
            n += j
        return n
print(add_all([1,2,3,4,5,6,7,8,9,10]))
# 리스트로는 계산되는데 튜플은 불가능. 값의 수정,삭제,삽입이 다 안되기 때문..
# 튜플도 가능하게 하는 법(아래)
def add_all2(*args):
    temp = 0
    for i in range(len(args)):
        if type(args[i]) == list:
            for j in args[i]:
                temp += j
        else:
            temp += args[i]
    return temp    
print(add_all2([1,2,3,4,5,6,7,8,9,10])) 
print(add_all2(1,2,3,4,5,6,7,8,9,10))


# 1부터 n까지 연속한 정수의 곱을 구하는 factorial값 구하기
def factorial(n):
    a = 1
    for i in range(1, n+1):
        a = i * a
    return a
print(factorial(5))  # 결과 120

# 선생님 풀이
# 재귀적으로 하는 것 
# for문을 사용하지 않고 함수 내에서 돌게 하는것을 재귀적으로 한다 라고 함
def fact(n):
    if n <= 1:  # n이 1 이하면 종료하는 조건
        return 1
    return n * fact(n-1)
print(fact(5))


# "대기번호 x번 이름"을 출력하고
# 번호표, 사람이름 원소로 이루어진 리스트 반환하기
people = ['펭수', '뽀로로', '뚝딱이', '텔레토비']
def func1(line):
    new_lines = []
    i = 1   # 대기번호 변수 i
    for x in line:
        print("대기번호 %d번 : %s" %(i,x))
        new_lines.append((i,x))
        i += 1  # 대기번호 업데이트
    return new_lines
list = func1(people)

# enumerte(열거하다)
# 반복 가능한 객체의 인덱스와 원소에 함께 접근할 수 있는 함수
# 자동으로 순번을 붙여줘서 많이 사용함
lst = ['a','b','c']
for x in enumerate(lst):
    print(x)
lst1 = 'abcd'
for x in enumerate(lst1):
    print(x)

# enumerate 적용한다면
people = ['펭수', '뽀로로', '뚝딱이', '텔레토비']
def func1(line):
    new_lines = []
    for idx, val in enumerate(line):
        print("대기번호 %d번 : %s" %(idx, val))
        new_lines.append((idx + 1, val))
    return new_lines
list = func1(people)


# zip
# 반복가능한 객체들을(2개 이상) 병렬적으로 묶어주는 함수
# 각 원소들을 튜플의 형식으로 묶어줌
str_list = ['one','two','three','four']
num_list = [1,2,3,4]

for i in zip(num_list, str_list):
    print(i)


# lambda
# 한 줄로 짤 수 있게하는 함수. 실행한 결과 값이 바로 반환값이 됨
# 단점은 변수 하나만 넣을 수 있음
def plus_two(num):
    return num + 2
# 위 함수를 lambda를 사용해서 한 줄로 짤 수 있음. 둘이 같은 코드
lambda x : x + 2

# map 
# 변수 하나만 넣을 수 있는 람다의 단점을 보완시켜줌
# 리스트, 튜플, 스트링 등 자료형 각각의 원소에 동일한 함수를 적용
# 프린트해서 확인하려면 list도 같이 사용해야함
items = [1,2,3,4,5]
squared_map = list(map(lambda x : x**2, items))
print(squared_map)

# lambda와 map를 사용해서 리스트에 있는 값을 str로 변경하기
items2 = [1,24,3,6,7]
str_items = list(map(lambda x : str(x), items2))
print(str_items)


# 리스트만들기
# 1.
li_1 = [0,1,2,3,4] 

# 2.
li_2 = []
for i in range(5):
    li_2.append(i)
print(li_2)

# 3.(new!) 한 줄로 짤 수 있는 방법이 추가되었다
li_3 = [i for i in range(5)]
print(li_3)


# 구구단 2단을 list comprehension을 이용하여 구현하고 리스트를 화면에 출력하기
# 함수 풀어써보기
def gugu(n):
    for i in range(1,10):
        print(n, "*", i, "=", n*i)
gugu(2)
# 풀어쓴걸 참고해서 한 줄로 줄여써보기
gugu = [2 * i for i in range(1, 10)]
print(gugu)


# for + if
# 10부터 20까지의 숫자들 중 짝수만을 담은 리스트를 만들어보기
list3 = []
for x in range(10,21):
    if x % 2 == 0:
        list3.append(x)
print(list3)
# 한 줄로 줄이기
lc_2 = [x for x in range(10,21) if x % 2 == 0]
print(lc_2)

# 1부터 10의 제곱수 중, 50 이하인 수만 리스트에 저장하기
lc_3 = [x**2 for x in range(1, 11) if x**2 < 50]
print(lc_3)

sentence = '코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 외출 시에는 마스크를 끼고, 손씻기를 생활화합시다.'
lc_4 = [s for s in sentence.split() if len(s) < 5]
print(lc_4)

# # 1부터 10까지의 숫자들 중 홀수이면 어떤 제곱수를, 짝수이면 세제곱수를 담은 리스트 만들기
list_4 = []
for x in range(1,11):
    if x % 2 == 1:
        list_4.append(x**2)
    else:
        list_4.append(x**3)
print(list_4)
[x**2 if x % 2 == 0 else x ** 3 for x in range(1,11)]

# 40 이하의 숫자는 5를 더하고, 40 초과의 숫자는 41로 바꾸어 리스트로 저장하고 리스트를 출력하기
list_5 = [12,67,32,48,19,57,29,49]
lc_5 = [x+5 if x <= 40 else 41 for x in list_5]
print(lc_5)


# # for문 + for문도 가능
# word1 = 'hello'
# word2 = 'world'
# result = [i+j for i in word1 for j in word2]
# print(result)
