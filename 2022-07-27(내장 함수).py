# 파이썬 내장 함수를 몇가지 알아보자

# 01. abs(x)은 어떤 숫자를 입력 받았을 때 절대값을 돌려주는 함수이다
from cgitb import reset


print(abs(-2))  # 2가 출력됨


# 02. all(x)는 반복 가능한 자료형(리스트, 튜플, 딕셔너리, 문자열, 집합 등으로 for문으로 출력이 가능한 것)을 인수로 받아 모두 참이면 True를, 하나라도 거짓이면 False를 돌려줌
print(all([1, 2, 3]))  # True 출력
print(all([1, 2, 3, 0]))  # False 출력(0은 False 즉 거짓을 의미함)

# 03. any(x)도 반복 가능한 자료형을 인수로 받는다. 그러나 이는 all과 반대로 하나라도 참이 있으면 True를 돌려주고, 하나라도 거짓이면 False를 돌려준다.
print(any([1, 0, 0]))  # True 출력
print(any([0, 0, 0]))  # False 출력
print(any([0, ""]))  # False 출력(공백도 거짓으로 처리함)

# 04.  chr(i)은 아스키 코드 값을 입력 받아 그 코드에 해당하는 값을 돌려준다
print(chr(97))  # 97은 영어 a를 의미함
print(chr(48))  # 48은 숫자 0을 의미함

# 05. dir은 객체가 차체적으로 가지고있는 변수나 함수를 보여줌
print(dir([1, 2, 3]))  # 리스트에 관련된 함수(메서드) 출력
print(dir({'1': 'a'}))  # 딕셔너리에 관련된 함수(메서드) 출력
# 위의 두 코드는 리스트, 딕셔너리에 관련된 함수(메서드)를 보여줌

# 06. divmod(a, b)는 a를 b로 나눈 몫과 나머지를 튜플 형태()로 돌려준다
print(divmod(7, 3))  # 몫은 2, 나머지는 1이다
print(divmod(8, 3))  # 몫은 2, 나머지는 2이다

# 07. enumerate(i)은 순서가 있는 자료형을 입력으로 받아 자료형의 현재 순서와 그 값을 알려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)  # 0 body, 1 foo, 2 bar가 출력됨

# 08. eval()은 실행 가능한 문자열(1+2, 'hi'+'a')의 결과값을 돌려줌
print(eval("'hi' + 'a'"))  # hia 출력

# 09. filter은 첫 번째 인수로 함수를 받고, 두 번째 인수로 반복 가능한 자료형을 받는다. 두 번째 인수의 요소가 첫 번째 인수에 들어갔을 때 결과 값이 참인 것만 걸러낸다
# 일반적인 출력


def positive(l):
    result = []
    for i in l:
        if i > 0:  # 0보다 큰 수만 뽑겠다
            result.append(i)
    return result


print(positive([1, -3, 2, 6, 0]))  # [1, 2, 6]이 출력됨

# filter 사용


def ps(x):
    return x > 0


print(list(filter(ps, [1, -3, 2, 6, 0])))  # 간단하게 했다.

# lamda 함수 사용
# lamda함수를 사용하여 더욱 간편하게 줄였다.
print(list(filter(lambda x: x > 0, [1, -3, 2, 6, 0])))

# 10. int()는 숫자를 입력 받아 그 수를 10진수로 변환하여 돌려준다.
print(int('11', 2))  # 2진수 11을 정수형으로 변환하겠다는 의미
print(int('1A', 16))  # 16진수 1A를 정수형으로 변환하겠다는 의미


# 11. isinstance(odject, class)는 object가 class의 인스턴스인지 확인하는 힘수임
class person:
    pass  # 클래스는 () 안 붙임


a = person()
print(isinstance(a, person))  # True기 출력됨

b = 3
print(isinstance(b, person))  # False 출력

# 12. map(f, iterable)은 반복 가능한 자료형을 함수에 넣어 실행시킨 결과를 묶어서 돌려줌
# 일반적인 출력


def mul(numlist):
    result = []
    for num in numlist:
        result.append(num * 2)
    return result


result = mul([1, 2, 3])
print(result)  # [2, 4, 6] 출력

# map함수 사용


def mul2(num): return num * 2


print(list(map(mul2, [1, 2, 3])))  # [2, 4, 6] 출력

# lamda 함수 사용
print(list(map(lambda x: x*2, [1, 2, 3])))  # [2, 4, 6] 출력


# 13. zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수임
print(list(zip([1, 2, 3], [4, 5, 6])))  # [(1, 4), (2, 5), (3, 6)]이 출력됨
print(list(zip("abc", "def")))  # [('a', 'd'), ('b', 'e'), (c'', f'')]
