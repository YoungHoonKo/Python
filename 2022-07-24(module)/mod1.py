# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

'''
print(add(1, 4))
print(sub(4, 2))
#이렇게 적으면 모듈을 호출할 때 결과 값이 출력된다. 함수를 출력하고 싶을 때는 밑의 코드를 확인하자
'''

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
   