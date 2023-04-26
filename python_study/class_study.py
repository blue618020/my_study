# 객체지향(oop, object oriented programmin)
# 객체와 객체 사이의 상호작용으로 프로그램을 
# 구성하는 프로그램의 패러다임

# 객체지향의 특징
# 추상화 : 공통된 속성이나 기능 도출 (특징을 남기는 작업)
# 캡슐화 : 데이터의 구조와 연산을 결합 (하나로 안에 합치는 느낌)
# 상속 : 상위 개념의 특징이 하위 개념(객체)에 전달 (물려주기와 유사)
# 다형성 : 유사 객체의 사용성을 그대로 유지 (새로운 하위 개념을 유지)

# 객체는 추상화와 캡슐화의 결과이다.
# 객체는 데이터 필드와 메소드를 가진다.

# 클래스는 객체를 정의한 것(객체의 설계도)
# 데이터 필드(멤버 변수, 속성)
# 객체가 가지고 있는 변수
# 메소드 : 객체가 가지고 있는 함수

# 예시) 붕어빵 틀(클래스) -> 만들어낸 붕어빵(객체) -> 포장지에 넣음(객체넣은 변수)

"""
class 클래스이름:
    클래스 멤버 변수
    메소드
"""
# 클래스 이름도 변수 이름 규칙을 지켜야 함
# 클래스 이름 컨벤션(관용. 선택이지만 지키는 편이 좋음)
# 첫 글자는 대문자
# 언더바(_)안씀
# 단어 구분할 때도 대문자
class Car:
    def move(self):
        print("move")
    # 클래스 안에 있는 함수(def)를 메소드, 멤버 함수라고 불림
    # 그리고 이 공간 안을 데이터 필드라고 함
    # 함수를 호출하려면 클래스를 먼저 호출해야 함
class SportsCar:
    pass

my_car = Car()
my_car.move()  # 결과 : move
# Car()를 하면 클래스가 객체로 만들어진거고(인스턴스)
# 그 객체를 my_car변수에 넣은 것
# . -> 객체 멤버 접근 연산자
li = [1,2,3,4,5]
li.append(6) #<-- 이런식으로 접근했던거

# 인스턴스
# 객체 중에서도 클래스를 통해 생성된 객체를 말함
# Car 클래스의 객체다 또는 인스턴스다 라고 함
# 사실 파이썬에서는 모든게 객체라고 볼 수 있다..!(순수객체지향)
# 그래서 . 을 통해 함수를 사용할 수 있던 것이였음

# 내장함수 type()
# 데이터의 자료형을 반환하는 함수(어디 클래스 소속인지 알 수 있음)
print(type(li))  # 결과 : <class 'list'> (리스트 클래스의 객체)
n = 10
print(type(n))   # 결과 : <class 'int'> (정수형 클래스의 객체)
print(type("hello"))  # 결과 : <class 'str'> (문자열 클래스의 객체)


# 자주쓰이는 문자열 메소드(함수)
# upper()
# 모두 대문자로 변경
s = "hello"
print(s.upper())   # 결과 : HELLO  

# lower()
# 모두 소문자로 변경
print(s.lower())   # 결과 : hello

# strip()
# 문자열 양쪽 끝의 특정 문자(공백같은거)를 제거
s1 = "   hello   "
print(s1.strip())   # 결과 : hello

# lstrin(), rstrin()
# 왼쪽, 오른쪽 끝의 특정 문자(공백같은거)를 제거
print(s1.lstrip())   # 결과 : hello
print(s1.rstrip())   # 결과 :    hello

# split()
# 구분자로 분할하여 리스트로 반환
s2 = "hello,world,python"
print(s2.split(','))   # 결과 : ['hello', 'world', 'python']

# replace('바꾸고 싶은 문자', '바꿀 문자')
# 문자열의 특정 부분을 대체
print(s2.replace(',',' '))  # 결과 : hello world python

# 문자열은 수정이 되지 않기 때문에(immutable) replace라는 함수를 사용하는 것
# 함수없이 그냥 출력해보면 , 이 붙어있는게 확인됨


# self 매개변수
# 무조건 모든 메소드의 첫번째 매개변수로 들어가야함
# 메소드의 정의에는 사용되지만, 호출에는 사용되지 않음
# 객체 자신을 참조하여 클래스에 정의된 멤버에 접근할 때 사용(가져다 쓴다던가)
class Person:
    def say(self):
        self.name = "사람1"
        print("Hello")
    def move(self):
        pass
    def eat(self, food):
        self.sleep()
        print(f"{self.name}이 {food}을/를 먹었습니다.")
    def sleep(self):
        print(f"{self.name}이 잠을 잤습니다.")

person1 = Person()
person1.say()
person1.eat("밥")

# initializer 초기자, 초기화기
# initialize 초기화(값을 가지게 만든다)
# refresh 초기화(싹 지우고 초기로)와는 다른 의미임 주의
# 초기화가 일어날때 초기자가 무엇을 할 것인지 정의하는 것

class Person:
    def __init__(self, name, age, gerder, phone):
        self.name = name  # 다른 def에서도 가져다 쓸 수 있게 정의한 것
        self.age = age
        self.gerder = gerder
        self.phone = phone
        print("initialize")

    def say_name(self):
        print(self.name)  # self를 이용해서 위의 변수를 데려옴

print("before")    # 초기자 전
person2 = Person("이름", 20, "남자", "010-1234-5678")  # 이니셜라이즈(초기화) 이루어짐
print("after")     # 초기자 후
person2.say_name()


# Person 클래스에 introduce 메소드를 추가
# 이름, 나이, 성별을 프린트하는 메소드
class Person : 
    def __init__(self, name, age, gerder):
        self.name = name  
        self.age = age
        self.gerder = gerder

    def say_name(self):
        print(self.name)

    def introduce(self):
        print(self.name, self.age, self.gerder)
        print(f"안녕하세요 저는 {self.name}입니다.")
        print(f"나이는 {self.age}세이고 성별은 {self.gerder}입니다.")

person2 = Person("김뫄뫄", 20, "남자")
person2.introduce()


# 상속 inheritance
# 하위 클래스가 상위 클래스에게 물려받는다
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name}가 생성되었습니다.")
    
    def say(self):
        print("")

class Dog(Animal): # 상속받을 클래스이름 입력. 안에 정의하지 않아도 상속받았기 때문에 그대로 사용 가능
    def say(self):
        print("멍멍")  # 또는 메소드를 재정의 할 수 있다. (method overriding)

my_dog = Dog("백구")
my_dog.say()

class Cat(Animal):
    def say(self):
        print("야옹")

my_cat = Cat("나비")
my_cat.say()

class Student:
    def __init__(self, name, age, school, grade):
        # 이름, 나이, 학교, 학년을 멤버 변수로 저장하는 메소드
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade
    
    def introduce(self):
        # 이름, 나이, 학교, 학년을 print 하는 메소드 정의
        print(f"{self.name}, {self.age}세, {self.school}, {self.grade}학년")

stu1 = Student("홍길동", 20, "서울대학교", 1)
stu2 = Student("손흥민", 21, "서울대학교", 2)
stu3 = Student("류현진", 22, "서울대학교", 3)
stu_list = [stu1, stu2, stu3]
for stu in stu_list:
    stu.introduce()
