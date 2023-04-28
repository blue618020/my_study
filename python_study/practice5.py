# 거꾸로 배열해도 같은 단어 또는 문장이 되는 
# 회문(palindrome)인지 판별하는 함수를 정의하세요
# 함수에 문자열을 입력받고 회문이면 True
# 아니면 False를 반환하도록 정의하세요
# 함수 이름 : is_palindrome
# 반환 값 : Ture 또는 False
# 기러기
# 소주 만병만 주소 
# 다시 합창합시다

def is_palindrome(input_string):
    # 방법1
    input_string = input_string.replace(" ","")  # 공백제거하고 다시 할당함
    length = len(input_string)  # 문자의 갯수 구하기. 
    for i in range(length//2):  # //2로 절반만 확인하기. 반만 검사해도 회문이란걸 알 수 있으니깜
        if input_string[i] != input_string[length - 1 - i]:
            return False
            # 앞에서부터 한글자씩 == 뒤에서부터 한글자씩 비교해서 맞지 않는 순간(!=) False 하고 탈출
        return True
    
    # 방법2 : 한줄로 간단하게 짤 수 있음
    # return input_string == input_string[::-1]
    # 정상 문자 == 뒤집은 문자 비교해서 바로 결과 리턴
    # [::-1]로 뒤집는 방법도 있음
result = is_palindrome("다시 합창합시다")    
print(result)

# 또다른 방법3
n1 = reversed("안녕하세요")
print(n1)
# 뒤집어진 >>새로운<< 문자열 출력 
# reverse()와는 조금 다른듯. 걔는 리스트 함수니깐
# 근데 프린트하면 출력결과가 안뜸..
# 확인할려면 for문으로 하나씩 까서 확인하는 방법이랑(비추) join을 사용하는것
n2 = "".join(reversed("안녕하세요"))
print(n2)
