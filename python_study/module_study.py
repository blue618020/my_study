# 모듈
# 함수, 변수, 클래스 모아놓은 파이썬 파일
# 다른 파이썬 프로그램에서 불러와서 사용
# import 명령어로 불러옴
# 모듈이름 = 파이썬 파일 이름
"""
import 모듈이름 
"""
import my_module
my_module.add(1, 2) 
my_module.sub(1, 2)
# 모듈도 객체.

"""
form 모듈이름 import 모듈함수
form 모듈이름 import 모듈함수1, 모듈함수2
form 모듈이름 import * (<<모두 다 가져오겠다)
"""
from my_module import add, sub
add(1, 2)
sub(1, 2)

from my_module import *
add(1, 2)
sub(1, 2)

# import my_module
# 이것만 쓰면 처음부터 모두 다 가져옴
# 그렇게 되면 필요없는것도 가져오게되는데, 그걸 방지해주는게 __name__=="__main__"
# 파이썬에서 정한 특별한 변수는 언더바 2개를 사용
# 프로그램 실행 시 작동
# 저 밑으로 들어가있는 코드는 출력되지 않음

from my_calculator import MyCalculator
my_calculator = MyCalculator()
my_calculator.div(10, 0)
# 0으로 나누면 에러가 나니깐 MyCalculator를 상속받아서 함수 재정의
class ZeroCalculator(MyCalculator):
    def div(self, n1, n2):
        if n2 == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            print(f"{n1} / {n2} = {n1/n2}")        
zero_calculator = ZeroCalculator()
zero_calculator.div(10,0)
# 에러를 미리 방지해주는게 중요하다. 나버리면 밑에 코드들은 다 수행이 안되니깐..

# 추가 기능
# ctrl + 코드 마우스 클릭
# 어디에 정의했는지 찾아들어갈 때 사용할 수 있음