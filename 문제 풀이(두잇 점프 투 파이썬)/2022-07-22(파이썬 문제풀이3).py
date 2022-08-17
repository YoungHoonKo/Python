'''
#1번 문제
def is_odd(number):
    if number % 2 == 1: return True
    else: return False
'''

'''
#2번 문제
def avg(*a):
    result = 0
    for i in a:
        result +=  i
    return result/len(a)
print(avg(1,2))
print(avg(1, 2, 3, 4, 5))
'''

'''
#3번문제
a = int(input('첫 번째 숫자를 입력해주세요 : '))
b = int(input('두 번째 숫자를 입력해주세요 : '))
total = a + b
print('두 수의 합은 %2d입니다.' % total)
'''

'''
#4번문제
print('a' 'b' 'c')
print('a'+'b'+'c')
print('a', 'b', 'c') #,는 띄어쓰기임
print("".join(['a' 'b' 'c']))
'''

'''
#5번
f = open('test.txt', 'w')
f.write('Life is too short')  #write를 print로 바꿔주면 됨(아님 절대 아님 절대 절대 아님)
f.close()

f1 = open('test.txt', 'r')
print(f1.read())
f1.close() #열었으면 꼭 닫아주자 닫아줘야지 출력이 된다.
'''

'''
#6번
a = input('저장할 내용을 입력하세요 : ')
f = open('test.txt', 'a')
f.write(a)
f.write('\n')
f.close
'''

'''
#7번
f = open('test.txt', 'r')
body = f.read()
f.close()
#print(body)

body = body.replace('java','python')

f = open('test.txt', 'w')
f.write(body)
f.close()
'''
