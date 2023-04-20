weather = "맑음"  # weather 변수에 값 할당
print("비가 오나요?", weather == "비")  # 문장 프린트, 변수와 문장이 같나 비교연산(True 출력)
if weather == "비":  # weather의 값이 같지 않아서 조건식이 False이므로 실행하지 않음
    print("우산을 가져간다.")  
elif weather == "맑음":  # weather의 값이 "맑음"과 같아서 조건식이 True이므로 안쪽 코드블록 실행
    print("날씨가 좋다.")
else:  # 조건식이 False이면 실행
    print("우산을 가져가지 않는다.")
