# dictinary(딕셔너리(사전)) 자료형
# key-value 형태
# key: value 
# 어떤 자료형이든 섞어서 넣을 수 있음

person = {
    "이름": "이름", 
    "나이": 18, 
    "점수": {
        "영어": 80, 
        "국어": 90, 
        "수학": 100
    }, 
    1: "일"
} 
print(person["나이"])
print(person["점수"]["영어"])

dict_1 = {1: 'a'}
dict_1['b'] = 2  # 'b': 2 로 key: value 쌍을 추가. 리스트와 방식이 조금 다름 
dict_1[1] = 'c'  # 'a'를 'c'로 변경
del dict_1[1]    # 1: 'a' 쌍을 완전 삭제
print(dict_1)


# 딕셔너리 함수의 종류

dict_2 = {1: 'a', 2: 'b', 3: 'c'}
# keys()
# 딕셔너리에서 key 값만 리스트 형태로 묶음
dict_key = dict_2.keys()
print(dict_key)
# 결과  dict_keys([1, 2, 3])

# values()
# 딕셔너리에서 value 값만 리스트 형태로 묶음
dict_values = dict_2.values()
print(dict_values)
# 결과  dict_values(['a', 'b', 'c'])

# item()
# 딕셔너리에서 key-value 쌍을 튜플로 묶어줌 (요런 소괄호를 튜플이라 부름)
dict_items = dict_2.items()
print(dict_items)
# 결과  dict_items([(1, 'a'), (2, 'b'), (3, 'c')])

# get(key)
# key에 대응되는 value를 돌려줌
# key값이 존재하지 않으면 None(데이터가 '없다'라는 의미의 데이터. 0)을 돌려줌
# print(dict_2["나이"] 로 하면 오류가 남 
print(dict_2.get("나이"))
# 결과  None
print(dict_2.get("나이", "나이불명")) # None 대신에 나이불명 이라는 값을 출력
# 결과  나이불명

# clear()
# 딕셔너리 안의 모든 요소를 삭제
dict_2.clear()
print(dict_2)
# 결과  {}

