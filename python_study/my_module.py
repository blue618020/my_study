def add(a, b):
    return a+b

def sub(a, b):
    return a-b

if __name__=="__main__": # 파이썬에서 특별한 변수는 언더바 2개__ 
    print(add(1,2))
    print(sub(3,4))
else:
    print(__name__)