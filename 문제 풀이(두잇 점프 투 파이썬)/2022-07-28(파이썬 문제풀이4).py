
# 1번 문제
import random


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)


# 2번 문제
class MaxLimitCalculator(UpgradeCalculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(70)
print(cal.value)


# 3번 문제

print(all([1, 2, abs(-3)-3]))  # 하나라도 거짓이면 False를 출력
print(chr(ord('a')))  # ord로 아스키 코드로 변횐 후, chr로 다시 문자로 변환함

# 4번 문제

# filter와 lamda를 이용해서 음수를 제거했습니다.
print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))

# 5번 문제

print(int('0xea', 16))  # 16진수를 10진수로 바꿨습니다.


# 6번 문제

# map 함수와 lamda 함수를 사용해서 3이 곱해진 리스트를 만들었습니다.
print(list(map(lambda x: x*3, [1, 2, 3, 4])))


# 7번 문제

a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(min(a)+max(a))  # 최대값과 최소값의 합을 구햇다 정답: -1


# 8번 문제

b = 17 / 3
print(round(b, 4))  # b의 값을 소수점 4자리까지 반올림 했다.


# 9번 문제


result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)
print(result)
