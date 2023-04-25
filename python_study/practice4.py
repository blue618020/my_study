# 다음 함수를 정의하세요.
# 정수 n을 입력받고, n보다 작은 수 중 
# 3의 배수와 5의 배수를 모두 더한 값을 반환하는 함수
# 함수 이름 : sum_3_5
def sum_3_5(n):
    result = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            result =+ i  
    return result
print(sum_3_5(10)) 


# 정육면체 주사위 2개가 있다. 
# 2개의 주사위를 던졌을 때 나올 수 있는 주사위 눈의 조합을 
# 모두 print 하는 함수를 정의하세요.
# 함수 이름 : double_dice
# 내 풀이
def double_dice():
    # for문
    for i in range(1,7):  # 1 ~ 6
        for j in range(1, 7):
            print(i, ",", j)
    i = 1
    # while문
    while i < 7:
        j = 1
        while j < 7:
            print(i, ",", j)
            j += 1 
        i += 1

    return i, j
double_dice()


# 두 수의 차이를 구하는 함수
# 함수에 입력된 두 정수의 차이를 계산하고 반환하는 함수를 정의하세요.
# 함수이름 : get_diff
# 내 풀이
def get_diff(a, b):
    result = abs(a - b)  # 음수 나오지 않게 절댓값 함수 사용
    # 방법 2
    # if a > b:
    #     result = a - b
    # else a < b:
    #     result = b - a
    return result
print(get_diff(2,4))


# 가장 큰 수를 만드는 함수
# 함수에 입력된 5개 정수(0 ~ 9, 증복가능)를 사용하며 
# 만들 수 있는 가장 큰 수를 반환하는 함수를 정의하세요.
# 함수 이름 : get_biggest
def get_biggst(a, b, c, d, e):
    numbers = [a, b, c, d, e]  # 리스트 만듬
    numbers.sort()  # 오름차순 정렬              
    result = 0
    for i in range(len(numbers)):  # 0 ~ 4까지
        result += numbers[i] * (10 ** i)  
        # 10진법으로 자릿수 설정(1,10,100,1000,10000 순서)
    return result

# 문자형으로 바꿔서 문자끼리 합칠 수도 있음
    # numbers = [a, b, c, d, e]
    # numbers.sort(reverse=True)  # 내림차순 정렬              
    # result = ""
    # for i in numbers:
    #     result += str(i)  # 문자형으로 변경
    # return int(result)    # 다 합친걸 정수형으로 바꿔서 반환

print(get_biggst(1,3,2,5,4))  # 결과 54321


# 별 찍기 2
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다. 
# 함수 이름 : print_stars2
"""
출력결과 
n -> 1
*
n -> 4
   *
  **
 ***
****
"""
# 내 풀이
def print_stars2(n):
    for i in range(1, n+1):
        print(" " * (n - i), "*" * i)
        # n -= 1
    print()
print_stars2(4)

# 피라미드
def print_stars3(n):
    for i in range(1, n+1):
        print(" "*(n-i),"*"*((2*i)-1))
    print()
print_stars3(4)
