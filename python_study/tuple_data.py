# tuple(튜플) 형
# element의 값이 한번 정해지면 수정할 수 없음
# mutable(수정 가능) / immutable(수정 불가능) 
# mutable에는 list, dict 
# immutable에는 int, float, str, tuple

my_list = [1, 2, 3]
my_list[0] = 5  # 값을 바꿀 수 있음(mutable)
print(my_list)  

my_tuple = (1, 2, 3)
my_tuple[0] = 5  # 할당이 안된다라고 에러남. 튜플형은 수정 불가능(immutable)
print(my_tuple)
tuple_1 = ("hello", "world", "python")
t2 = (1, 2, 3, 4, 5)
t3 = (1, 2, "hello")
t4 = 1, 2, 3
t5 = (1, 2, (3, 4, 5))
# 자료형에 구애받지않고 뭐든지 넣기 가능. ()빼고도 사용가능한데 가독성을 위해 넣는 편이 좋다
# 리스트랑 같은 기능이지만 값 수정이 불가능하다는게 다름

t6 = tuple_1 + t2
t7 = t3 * 3
# 연결하거나 반복해서 "새로운" 튜플을 만드는거라 문자열 연산자는 됨

t3 = (1, 2, "hello")
print(t3[2])    # 데이터 타입: str 수정가능
print(t3[0:2])  # 튜플에 슬라이싱을 하게 되면 튜플 상태로 가져옴. 데이터 타입: tuple 수정불가능
print(len(t3))  # 수정가능

t5 = (1, 2, (3, 4, 5))
print(t5[2][1])

t8 = (5, 3, 1, 4, 2)  
# 순서대로 정렬 불가능. 안의 값이 바뀌니깐
# 리스트에서 사용했던 함수들도 다 불가능함(길이구하는 len()빼고)
for i in t8:
    print(i)
    # 123순서가 아닌 인덱스 순서대로 출력됨

# 2 ~ 9사이의 숫자를 입력받아 해당하는 단의 구구단을 출력하세요
# 2 ~ 9사이의 숫자가 아닌 값이 입력된 경우, 잘못입력되었다고 출력하고 다시 입력받으세요
# 내 풀이
while True:
    n = int(input("단 입력:"))
    if n >= 2 and n <= 9:
        for i in range(1, 10):
            print(n, "*", i ,"=", n*i)
    else:
        print("다시입력해주세요")
        continue  
    user_input = input("종료하려면 0을 입력: ")
    if user_input == "0":
        break

#  선생님 풀이
# n <= 2 and n <= 9 ----> 2 ~ 9 사이라면 True
n = int(input("단 입력:"))
while not 2 <= n <= 9:  # not을 써서 올바르게 입력하지 않는 경우를 잡아낼려고(False)
    print("2 ~ 9 사이의 숫자를 입력해주세요.")
    n = int(input("단 입력:"))
for i in range(1, 10):  # while의 조건이 Ture면 이쪽으로 넘어와서 구구단 출력
    print(n, "*", i ,"=", n*i)

# for i in range(9):
#     print(n*(i+1)) 이것도 가능
# 선생님의 풀이가 더 간결하고 간단한 느낌.. 하나배웟다

# 정수를 입력받고
# 그 정수보다 작은 수 중 가장 큰 제곱수를 출력하세요 
# ex) 10입력 > 출력 9, 11입력 > 출력 9
n = int(input("정수 입력: "))
i = 1
while True:
    # i ** 2 == i * i 
    if i ** 2 >= n:
        break
    answer = i ** 2
    i += 1
print("제곱수:",answer)

# [1, 2, 3, 4, 5]
# [10, 20, 30, 40, 50]
# [532, 5941, 54682, 58, 5]
# 3개의 리스트에서 같은 인덱스의 값끼리 더하여 출력하세요.
# 내 풀이
a1 = [1, 2, 3, 4, 5]
b1 = [10, 20, 30, 40, 50]
c1 = [532, 5941, 54682, 58, 5]
for i in range(len(a1)):  # 길이가 정해져 있으니 5 넣어도 됨
    print(a1[i] + b1[i] + c1[i])

# zip()
# 길이가 같은 list를 묶어서 for문 등으로 사용가능한 iterable을 반환함
a1 = [1, 2, 3, 4, 5]
b1 = [10, 20, 30, 40, 50]
c1 = [532, 5941, 54682, 58, 5]
for x, y, z in zip(a1, b1, c1):
    print(x + y + z)
# [[1, 10, 532], [2, 20, 5941]..]이런식으로 묶인 것! --> [x, y, z]

# whlie문으로도 풀이
i = 0
while i < 5:
    print(a1[i] + b1[i] + c1[i])
    i += 1  # 요 문에서만 넣으면 되는구나 for문에선 굳이 필요없음

# 정수를 입력받고 1부터 입력받은 정수까지 모두 출력하세요.
# 단, 3의 배수를 출력하는게 아닌 숫자에 3, 6, 9가 들어있는 경우 숫자 대신 짝이라고 출력하세요.
# 931 % 100 = 900 빼오기 
# 31 // 10 == (931 % 100) // 10 = 30 빼오기 그렇구낭......
n = int(input("정수 입력: "))
for i in range(1, n + 1):
    answer = i
    for j in str(i):  # 숫자를 str형으로 변경. 문자가 된 숫자를 하나씩 가져올 수 있게 됨 예) 931 > "931"
        if int(j) % 3 == 0 and j != '0':
            answer = "짝"
            break
    print(answer)

# 정수를 입력받고 그 정수의 약수를 모두 출력하세요.
# 약수 : 나누었을 때 나머지가 0으로 나누어 떨어지게 하는 수
n = int(input("정수 입력: "))
# 방법 1
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
# 방법 2
i = 1 
while i <= n:
    if n % i == 0:
        print(i)
    i += 1

