class FourCal():
    # 생성자 객체(self)에 초기값을 설정해야할 필요가 있을 때 객체가 생성되면 자동으로 호출되는 생성자를 쓰는 것이 좋음
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):  # 클래스 상속
    def pow(self):
        result = self.first ** self.second
        return result


class safeFourCal(MoreFourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            self.first / self.second


#b = MoreFourCal(2, 3)
# print(b.add())
#a = FourCal(2, 1)
#a.setdata(1, 2)
# print(type(a))
# print(a.first)
# print(a.second)
a = safeFourCal(2, 0)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(a.pow())


class Family:
    lastname = 'Ko'


print(Family.lastname)
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
Family.lastname = "박"
print(a.lastname)
print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))
# 세 함수는 주소가 모두 같다 즉 같은 메모리를 가리킴
