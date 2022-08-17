# render.py
#from ..sound.echo import echo_test # 연관(relative)를 이용한 모듈 호출임 ..은 부모 디렉터리를 의미함.
from game.sound.echo import echo_test #render.py에서 다른 모듈을 사용하고 싶을 때 이렇게 한다.
def render_test():
    print('render')
    echo_test()
