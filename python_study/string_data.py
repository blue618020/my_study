# print("안녕하세요."+"반갑습니다.")
# print("안녕하세요"*5)
# print("안녕하세요"+10) 에러 문자열+숫자 

# 인덱싱 실습
# print("hello"[0])
# print("hello"[1])
# print("hello"[2])
# print("hello"[3])
# print("hello"[4])
# print("hello"[-1]) # hello 라는 범위를 정한 상태로 하기 때문에 -1을 쓰면 맨 뒤의 문자가 나오게 됨(-5까지 가능)

# 슬라이싱 실습
# print("hello"[1:3]) # [첫 인덱스:끝 인덱스]
# print("hello"[2:4])
# print("hello"[:3]) # 앞 공백은 처음부터로 지정됨
# print("hello"[2:]) # 뒤 공백은 끝까지로 지정됨

# print("hello"[100]) # 100칸은 범위를 넘어갔기 때문에 에러가 남. Error out of index

print(len("hello")) # 문자의 길이를 알아내는 함수
