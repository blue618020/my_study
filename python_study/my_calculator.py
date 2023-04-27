# 계산기 만들기
# 기능 : 두 정수의 사칙연산(+, -, *, /)
# add(), sub(), mul(), div() 함수 정의 
# input()함수를 활용하여 정수 2개, 사칙연산 선택을 입력받은 후 
# 계산 결과를 프린트한다.
# 계산식과 결과를 
# calculator_result.txt 파일에 기록한다.
# 사용자가 'q'를 입력하면 종료한다.

# 첫번째, 계산과 파일에 기록하는 함수를 정의
# def add(a, b):
#     result = str(a)+" + "+str(b)+" = "+str(a+b) 
#     print(result)
#     with open("python_study/calculator_result.txt", 'a', encoding="utf=8") as f:
#             f.write(result)

# def sub(a, b):
#     result = str(a)+" - "+str(b)+" = "+str(a-b)
#     print(result)
#     with open("python_study/calculator_result.txt", 'a', encoding="utf=8") as f:
#             f.write(result)
    
# def mul(a, b):
#     result = str(a)+" * "+str(b)+" = "+str(a*b)
#     print(result)
#     with open("python_study/calculator_result.txt", 'a', encoding="utf=8") as f:
#             f.write(result)
    
# def div(a, b):
#     result = str(a)+" / "+str(b)+" = "+str(a/b)
#     print(result)
#     with open("python_study/calculator_result.txt", 'a', encoding="utf=8") as f:
#             f.write(result)
    
# # 두번째, 함수 호출해서 계산 출력
# while True:
#     print("""
#     계산기
#     1: + 
#     2: -
#     3: *
#     4: /
#     q: 종료
#     """)
#     operator = input("원하는 계산을 입력하세요 :")
#     if operator == 'q':
#        print("종료했습니다.")
#        break
#     a = int(input("정수 1 :"))
#     b = int(input("정수 2 :"))
#     if operator == "1":
#         add(a, b)
#     elif operator == "2":
#         sub(a, b)
#     elif operator == "3":
#         mul(a, b)
#     elif operator == "4":
#        div(a, b)


# 20230426 추가.
# MyCalculator 클래스로 만들어보기
# add, sub, mul, div 메소드
class MyCalculator:     
    def __init__(self):
        pass

    def add(self, n1, n2):
        print(f"{n1} + {n2} = {n1+n2}")

    def sub(self, n1, n2):
        print(f"{n1} - {n2} = {n1-n2}")

    def mul(self, n1, n2):
        print(f"{n1} * {n2} = {n1*n2}")

    def div(self, n1, n2):
        print(f"{n1} / {n2} = {n1/n2}")

if __name__=="__main__":
    my_calculator = MyCalculator()
    while True:
        print("""
            계산기
            1: + 
            2: -
            3: *
            4: /
            q: 종료
        """)
        operator = input("원하는 계산을 입력하세요 :")  
        if operator == 'q':
            print("종료했습니다.")
            break
        n1 = int(input("정수 1 :"))
        n2 = int(input("정수 2 :"))
        if operator == "1":
            my_calculator.add(n1, n2)
        elif operator == "2":
            my_calculator.sub(n1, n2)
        elif operator == "3":
            my_calculator.mul(n1, n2)
        elif operator == "4":
            my_calculator.div(n1, n2)       
