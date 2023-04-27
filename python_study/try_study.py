# 예외 처리
# 오류 발생을 잡아내서 처리하는 것

# # 인덱스 에러
# li = [1,2,3,4,5]
# li[100]

# 제로 디비전 에러
# 100 / 0

# 파일 없음 에러
# f = open("없는파일", "r")

# 에러 발생 시 프로그램을 중단하고 에러 메세지를 보여줌


# 예외 처리 구문
# try ~ except
# try 블록에는 오류가 발생할 수 있는 코드
# except 블록에는 오류가 발생했을 때 수행할 코드
# 오류가 발생하지 않으면 except 블록의 코드는 실행되지 않음
try:
    100 / 0
except:
    print("에러 발생")
print("에러발생 후")

# Exceptio : 오류 객체(클래스)
# e : 에러 메세지 출력
try:
    100 / 0
except Exception as e:
    print(e)
print("에러발생 후")

# ZeroDivisionError : 에러 중에 해당을 특정해서 넣은 것
# 특정한거라 다양한 에러를 잡아낼 수는 없음(Exceptio 쓰는게 낫다)
# e 뒤에 원하는 문자를 넣을 수 있음
try:
    [1,2,3,4,5][100]
except ZeroDivisionError as e:
    print(e, "0으로 나눌 수 없습니다.")
except IndexError as e:
    print(e, "인덱싱할 수 없습니다.")
print("에러발생 후")

# finally
# 예외 발생 여부와 상관없이 항상 수행되는 코드
try:
    f = open("없는파일","r")
except:
    print("에러 발생")
finally:
    f.close()

# else
# 오류가 발생하지 않으면 실행되는 코드
try:
    age = int(input("나이:"))
except:
    print("입력이 잘못되었습니다.")
    print("숫자를 입력해주세요.")
else:
    if age > 20:
        print("성인입니다.")
    else:
        print("미성년자입니다.")

# 예외를 발생시키기
# raise 에러객체
class Bird:
    def fly(self):
        raise NotImplementedError
        # 코드 구현이 되지 않았다 라고 에러를 발생시킴
my_bird = Bird()
my_bird.fly()
     