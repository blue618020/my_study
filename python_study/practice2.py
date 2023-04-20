li_1 = ["Hello", "World", "Python"]
# li_1의 원소를 사용하여
# Hello World Python 이라고 출력하세요.
# 방법1
print(li_1[0], li_1[1], li_1[2]) 
# 방법2 
# join(리스트) 
# 리스트의 문자열을 합치는 함수
print(" ".join(li_1))  # li_1 리스트 안에 있는 문자열 사이에 공백" "을 넣어서 합치라는 뜻
# join이랑 같음 방법3
print(li_1[0] + " " + li_1[1] + " " + li_1[2]) 

# li_1의 원소를 사용하여
# HelP라고 출력하세요.
print(li_1[0][0:3] + li_1[2][0]) # Hello 중에 Hel만, Python 중에 P만 가져오기 위해 슬라이싱을 응용한 것!

li_2 = [1, 2, 3]
# li_1과 li_2를 사용하여
# ["Hello", "World", "Python", 1, 2, 3] 을 출력하세요
# 방법1
print(li_1 + li_2)
# 방법2
li_1.extend(li_2)
print(li_1)

# li_1과 li_2를 사용하여
# ["Hello", 1, "World", 2, "Python", 3] 을 출력하세요
li_1.insert(1, li_2[0])
li_1.insert(3, li_2[1])
li_1.insert(5, li_2[2]) # 또는 li_1.append(li_2[2])
print(li_1)


scores = []
scores.append(int(input("영어 점수: ")))  
scores.append(int(input("국어 점수: ")))  
scores.append(int(input("수학 점수: ")))  
# input으로 숫자를 입력받으면 문자열이기 때문에 int 타입으로 변경
# 그리고 입력한 수는 append 함수를 통해 scores 리스트에 추가됨

avg = (scores[0] + scores[1] + scores[2]) / 3
# sum()
# 리스트의 요소를 모두 더함
# 문자가 리스트 안에 섞여있으면 에러남
# avg = sum(scores)/3 이렇게도 가능

print(avg)
if avg >= 91:
    print("A")
elif avg >= 81:
    print("B")
elif avg >= 71:
    print("C")
elif avg >= 61:
    print("D")
else:
    print("F")


# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건을 몇개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 500원이다.
"""
# 내 풀이
age = int(input("나이: "))
money = int(input("가진 돈: "))
mm = money // 500
uu = money % 500
print("살 수 있는 물건의 개수:", mm, "개") 
print("잔돈:", uu, "원") 
"""
# 선생님 풀이
age = input("나이: ")
money = int(input("돈: "))
price = 500
print(money // price)  # 몫 연산자 사용
print(money % price)   # 나머지 연산자 사용

# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건별로 각각 몇개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 1000원이다.
# 2번 물건은 50원, 3번 물건은 120원이다.
"""
# 내 풀이 (이것도 맞긴한데 몫과 나머지를 따로 구하면 변수의 갯수가 너무 늘어나서 비효율적)
mm = [1000, 50, 120]
age = (int(input("나이: ")))  
money = (int(input("가진 돈: ")))  
m_1 = money//mm[0]
m_2 = money//mm[1]
m_3 = money//mm[2]
print("1000원 물건:", m_1, "개")
print("500원 물건:", m_2, "개")
print("120원 물건:", m_3, "개")
...
"""
#선생님 풀이 (요게 제일 간단심플 효율적)
age = input("나이: ")
money = int(input("돈: "))
price = [100, 50, 120]
print(money // price[0], money % price[0]) 
print(money // price[1], money % price[1]) 
print(money // price[2], money % price[2]) 

# 거스름돈은 어케하지
# ㄴ몫 연산자와 나머지 연산자를 사용하면 해결되는구나..!