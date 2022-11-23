'''
# 더할 횟수를 정하고 더한 값을 차례대로 출력함
import sys
N = int(input(''))
M = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    M.append(a + b)
for j in range(N):
    print(M[j])
'''

'''
# 위의 코드롸 값음(업그레이드 버전)
import sys

N = int(input(''))
M = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    M.append(a + b)

for j in range(N):
    print("Case #%d: %d" % (j+1, M[j]))
'''

'''
t=int(input(""))

for i in range(1,t+1):

      a, b=map(int,input().split())

      print("Case #%s: %s + %s = %s" %(i,a,b,a+b))
'''