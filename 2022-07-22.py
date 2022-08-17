'''
#입력값과 결과값이 있는 함수
def add(a, b):
    return a + b

a = 1
b = 2
print(add(a, b))


#입력값이 없는 함수
def say():
    return 'Hi'
print(say())

#결과값이 없는 함수(결과값은 오직 return으로만 돌려받을 수 있음)
def add2(a, b):
    print('%d + %d = %2d' %(a, b, a+b))  #이 문장은 함수의 구성요소인 수행할 문장의 일부분일 뿐임
print(add2(1, 2))


#입력값과 결과값이 둘 다 없는 함수
def say2():
    print('Hi')
print(say2())
'''

'''
def add(a, b):
    return a + b
print(add(3, 4))

result = add(a=1, b=8) #매개변수 지정하여 호출하기
print(result)
'''

'''
#입력값이 몇 개인지 모를 때(리스트로 뱐헤서 나온다.)
def add(*a):
    result = 0
    for i in a:
        result += i
    return result
print(add(1, 2, 3, 4, 5))
'''

'''
def cal(choice, *a):
    if choice == 'add':
        result = 0
        for i in a:
            result += i
    elif choice == 'mul':
        result = 1
        for i in a:
            result *= i
    return result

print(cal('add', 1, 2, 3, 4, 5))
print(cal('mul', 1, 2, 3, 4))
'''

'''
#키워드 파라미터
def print_kwarge(**args):  #매개변수 앞에 **을 붙여주면 됨
    return args
    
print(print_kwarge(a = 1)) 
print(print_kwarge(name = 'yh', age = 20))
#두 함수의 결과값은 딕셔너리 형태로 변환되어서 나옴
'''

'''
def say_myself(name, age, man = True):
    print("이름은 %s입니다." % name)
    print('나이는 %d입니다.' % age)
    if man: print('남자입니다.')
    else: print('여자입니다.')
print(say_myself('영훈', 20)) #아무것도 안 넣으면 True로 인식함
print(say_myself('영훈', 20, True))
#위의 두 함수는 같음
#매개변수를 지정할 때는 맨 뒤로 뺀다.
'''

'''
add = lambda a, b: a + b
res = add(1, 2)
print(res)
#def함수를 못 쓰거나 쓰지 않고 간결하게 만들 수 있음
'''

'''
a=1
def vartest(a):
    a += 1
    
print(vartest(a))  #함수값이 없는 것 아닌가? 함수에서 돌려주지 않았는데 어떻게 1이라는 숫자가 나오지?? print는 전역변수 a를 사용해서 출력함. vartest는 return값이 존재 x
print(a)
'''

'''
a=1
def vartest(a):
    a += 1
    return a

print(vartest(a)) #함수 안의 변수가 return으로 반한됐기 때문에 함수 안의 값을 함수 밖에서도 사용할 수 았다.
print(a) #여전히 전역변수 a를 사용하기 때문에 아무런 변화가 없음
a = vartest(a) 
print(a) #함수의 출력값을 전역변수 a에 저장했다. 그래서 전역변수 a가 변해서 print의 값이 달라졌다
'''

