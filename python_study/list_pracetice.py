"""
학생1 : 영어 100, 국어 100
학생2 : 영어 90, 국어 80
학생3 : 영어 70, 국어 80
학생4 : 영어 50,국어 100
학생5 : 영어 30, 국어 20
"""
# 리스트 1
students = ["학생1", "학생2", "학생3", "학생4", "학생5"]
english_scores = [100, 90, 70, 50, 30]
korean_scores = [100, 80, 80, 100, 20]
print(students[0])
print(english_scores[0])
print(korean_scores[0])

# 리스트 2
students_info = [
    ["학생1", 100, 100]
    ["학생2", 90, 80]
    ["학생3", 70, 80]
    ["학생4", 50, 100]
    ["학생5", 30, 20]
]
print(students_info[0])

# 상황에 맞게 원하는 방식으로 쓰면 됨. 중요한건 이걸 쓴 개발자는 어떤 정보였는지 기억하고 기록해두는 것