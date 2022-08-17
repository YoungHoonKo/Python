# 점프투파이썬 2장 연습문제

'''
#1번
a = 80
b = 75
c = 55
d = (a + b + c) / 3
print(d)
'''

'''
#2번
a = 13
if a % 2 ==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
'''

'''
#3번
pin = "881120-1068234"
yyyymmdd = list(pin[0:6])
num = list(pin[7:])
print(yyyymmdd)
print(num)
'''

'''
#4번
pin = "881120-1068234"
print(list(pin[7:8]))
'''

'''
#5번
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)
'''

'''
#6번
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)
'''

'''
#7번
a = ["Life", "is", "too", "short"]
result = " ".join(a)
print(result)
'''

'''
#8번
a = (1, 2, 3)
a = a + (4,) #하나만 사용할 때는 (5,) 처럼 ,을 붙여준다.
print(a)
'''

'''
#10번
a = {'a':90, 'b':80, 'c':70}
result = a.pop('b')
print(a)
print(result)
'''

'''
#11번
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)  #리스트를 집합 자료형으로 변환함
b = list(aSet)  #집합 자료형을 리스트 자료형으로 다시 변환
print(b)
'''

'''
#12번
a = b = [1, 2, 3]
a[1] = 4
print(b)
'''
