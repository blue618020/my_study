# my_calculator 모듈의 MyCalculator 클래스를 상속받아서
# MaxLimitCalaulator 클래스를 정의하세요.
# add, sub, mul, div 메소드를 사용하여
# 더하기, 빼기, 곱하기, 나누기를 할 수 있다.
# 0으로 나눴을 때 에러가 발생하지 않도록 처리한다.
# 입력되는 정수 1개라도 100보다 크면 계산하지 않고 
# 100 이하의 값을 입력하도록 안내 메시지를 출력한다.
# 계산 결과가 100보다 크면 계산하지 않고 
# 100 이하의 결과가 나오는 값을 입력하도록 안내 메시지를 출력한다.

from my_calculator import MyCalculator
class MaxLimitCalaulator(MyCalculator):
    # 상속받은 부모 코드에서 덮어씌우는거라 실행시키면 이 코드가 작동됨
    def add(self, n1, n2):
        if n1 > 100:
            print("100이하의 값을 입력하세요.")
        elif n2 > 100:
            print("100이하의 값을 입력하세요.")
        else:
            result = n1 + n2
            if result > 100:
                print("100이하의 결과가 나오는 값을 입력해주세요.") 
            else:
                print(f"{n1} + {n2} = {n1+n2}")

    def sub(self, n1, n2):
        if n1 > 100:
            print("100이하의 값을 입력하세요.")
        elif n2 > 100:
            print("100이하의 값을 입력하세요.")
        else:
            result = n1 - n2
            if result > 100:
                print("100이하의 결과가 나오는 값을 입력해주세요.") 
            else:
                print(f"{n1} - {n2} = {n1-n2}")

    def mul(self, n1, n2):
        if n1 > 100:
            print("100이하의 값을 입력하세요.")
        elif n2 > 100:
            print("100이하의 값을 입력하세요.")
        else:
            result = n1 * n2
            if result > 100:
                print("100이하의 결과가 나오는 값을 입력해주세요.") 
            else:
                print(f"{n1} * {n2} = {n1*n2}")

    def div(self, n1, n2):
        if n1 > 100:
            print("100이하의 값을 입력하세요.")
        elif n2 > 100:
            print("100이하의 값을 입력하세요.")
        # elif n2 == 0:
        #     print("0으로 나눌 수 없습니다.")
        else:
            try:
                result
            except ZeroDivisionError:
                print("0으로 나눌 수 없습니다.")
            result = n1 / n2
            if result > 100:
                print("100이하의 결과가 나오는 값을 입력해주세요.") 
            else:
                print(f"{n1} / {n2} = {n1/n2}")     

my_max_limit_calculator = MaxLimitCalaulator()  # 이니셜라이즈. 새로 만듬
my_max_limit_calculator.add(100,20)
