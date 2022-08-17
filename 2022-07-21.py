
'''
money = True

if money:
    print("taxi")
else:
    print("walk")
'''

'''
a = int(input("입력해주세요 : "))
card = True

if a >= 3000 and card:
    print("taxi")
else:
    print("walk")
'''

'''
a = [1, 2, 3, 4, 5]
print(1 in a)
print(7 not in a)

b = ['a', 'b', 'c', 'd']
print('a' in b)
print('b' not in b)
'''

'''
poket = ['money', 'phone', 'wallet']

if 'money' in poket:
    print("taxi")
else:
    print("walk")
'''

'''
poket = ['money', 'phone']

if 'caard' not in poket:
    print("walk")
else:
    print('bus')
'''

'''
poket = ['phone']

if 'money' in poket:
    pass
else:
    print('find card')
'''

'''
a = int(input('number : '))

if a > 20: pass
else: print('lower than 20')
'''

'''
#조건부 표현식
score = int(input(':'))

print('success') if score > 70 else print('failure')
'''

'''
treeHit = 0

while treeHit < 10:
    treeHit += 1
    print('나무를 %d번 찍었습니다' % treeHit)
    if treeHit == 10: print('나무가 넘어갑니다.')
'''

'''
coffee = 10
a = 10

while True:
    money = int(input('300원을 넣어주세요 : '))
    if money == 300:
        print('완성입니다.')
        coffee -= 1
        print('잔여 커피량 : %d' %coffee)
        if coffee == 0:
            print('죄송합니다 커피가 다 떨어졌습니다.')
    elif money < 300:
        print('돈이 부족합니다.')
        addMoney = 300 - money
        print('%d원을 더 넣어주세요' %addMoney)
    elif money > 300:
        change = money - 300
        print('거스름돈은 %d입니다' %change)
'''

'''
for i in range(1, 11):
    if i % 3 != 0:
        print(i)
'''

'''
score = [50, 24, 90, 85, 60]
number = 0
for i in score:
    number += 1
    if i >= 60:
        print('number %d : pass' %number)
    else:
        print('number %d : nonpass' %number)
'''

'''
score = [50, 24, 90, 85, 60]
number = 0
for i in score:
    number += 1
    if i < 60: continue
    print('number %d, congratulation you pass the exam' %number)
'''

'''
score = [50, 24, 90, 85, 60]
for i in range(len(score)):
    if score[i] < 60: continue
    print('number %d, you pass the exam' %(i+1))
'''

'''
add = 0
for i in range(1, 101):
    add = add + i
print(add)
'''

'''
for i in range(2, 10):
    print("%d단" % i)
    for j in range(1, 10):
        print('%dX%d=%2d' % (i, j, i*j), end='\t')
    print('', end='\n')
'''

'''
a = [1, 2, 3, 4, 5]
result = []
for num in a:
    result.append(num*3)
print(result)
'''

'''
a = [1, 2, 3, 4, 5]
result = [num*3 for num in a]
print(result)
'''

'''
a = [1, 2, 3, 4, 5]
result = [num*3 for num in a if num % 2 == 0]
print(result)
'''

'''
result = [x*y for x in range(2, 10)
          for y in range(1, 10)]
print(result)
'''

'''
i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)
'''
