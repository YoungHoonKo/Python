import imp
import mod1 #모듈을 호츌하는 것으로 모듈이름과 함수를 적어줘야한다.
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

from mod1 import add #모듈 이름 없이 사용하고 싶을 때 이렇게 적는다
print(add(3, 4)) 

from mod1 import add, sub #한 모듈 안에 여러가지 함수가 있을 때 원하는 함수를 꺼내서 쓸 수 있다

from mod1 import * # *은 파이썬에서 모든 것이라는 뜻이다. 함수에서 변수를 몇개 받을지 모를때 *을 사용했다(기억하기)

import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))


#반지름이 5인 원의 넓이는??
import mod2
a = mod2.Math()
print(a.solv(5))