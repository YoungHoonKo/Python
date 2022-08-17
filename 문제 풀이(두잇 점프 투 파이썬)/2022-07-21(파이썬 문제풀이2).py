# 점프투파이썬 3장 연습문제 풀이

'''
#1번
a = "Life is too short, you need python"
if 'wife' in a: print('wife')
elif 'python' in a and 'you' not in a: print('python')
elif 'shirt' not in a: print('shirt')
elif 'need' in a: print('need')
else: print('none')
'''

'''
#2번
result = 0
num = 1
while num <= 1000:
    if num % 3 == 0:
        result += num 
    num += 1
print(result)
'''

'''
#3번
i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)
'''

'''
#4번
i = 0
for i in range(1, 101):
    print(i, end='\n')
'''

'''
#5번
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for i in a:
    total += i
average = total / len(a)
print(average)
'''

'''
#6번
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 != 0]
print(result)
'''
