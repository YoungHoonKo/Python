import imp
from operator import ipow
import re
import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo.echo_test()

from game.sound import *
echo.echo_test()

# *을 사용하여 render.py 파일 안의 render_test.py 사용해보기
from game.graphic import *
render.render_test()

