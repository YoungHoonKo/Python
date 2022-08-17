'''
# 오류 메시지 e는 내장되어 있다. 발생 오류에 따라 오류 메시지가 변경된다.
from decimal import DivisionByZero
from logging import exception

# 예외 처리 기법
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
    
# try문에서 오류가 발생해야지 except문을 실행한다.


# IndexError가 발생할 때 오류 메시지를 츌력하는 코드
a = [1, 2, 3]
try:
    print(a[4])
except IndexError as e:
    print(e)
    
# 여러 개의 오류 처리하기
try:
    a = [1, 2]
    print(a[4])
    4 / 0
    
except IndexError:
    print('인덱싱할 수 없음')
except DivisionByZero:
    print('나눌 수 없음')
# try에 적힌 순서대로 오류를 체크함, 그래서 인덱싱 오류가 먼저 검출됨, 인덱싱 오류가 먼저 발생했으므로 4 / 0 오류는 발생하지 않은 것

try:
    a = [1, 2]
    print(a[4])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)
# 두 개의 오류를 한 번에 처리하는 방법





# 오류 일부러 발생시키기
# 상속에서 많이 쓰임

class Bird:
    def fly(self):
        raise NotImplementedError
    

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()    
# Eagle에 fly 함수가 없다. 그래서 상속 받은 Bird에 있는 fly 함수를 가져온다.

class Pigeon(Bird):
    def fly(self):
        print('slow')
pigeon = Pigeon()
pigeon.fly()
# fly함수를 독자적으로 만들었기 때문에 Pigeon 안에 있는 fly 함수가 실행됨
'''


# 예외 만들기
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


print(say_nick('천사'))
# print(say_nick('바보'))
'''
try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print('허용되지 않는 별명입니다')
'''

# 오류 메시지르 사용하고 싶을 때 사용함
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
