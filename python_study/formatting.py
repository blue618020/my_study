# 문자열 포미팅(formatting)
# 여러가지 타입을 한번에 같이 쓰기 위해 사용
# result = str(a)+" + "+str(b)+" = "+str(a+b)를 짧게 만들어본다면
result = "%d + %d = %d" % (3, 2, 5)
print(result) 
a, b = 1, 2
result = "%d + %d = %d" % (a, b, a+b)
print(result)

# 포맷 코드
# %s 문자열(string)
# %d 정수(int)
# %f 실수(float)
# %o 8진수
# %x 16진수
# %% %글자 자체

string1 = "hello"
int1 = 3
float1 = 1.2345
print("%s %d %f" % (string1, int1, float1))

# f-string
# 유용하게 잘 쓰이는 강력한 기능!
# python 3.6 이후 버전부터 지원
result = f"{string1} {int1} {float1}"
print(result)
