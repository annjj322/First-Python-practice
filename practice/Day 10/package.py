# 모듈들을 모아둔 집합

import travel.thailand # class나 함수를 따로 import 할 수 없다.
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # 이렇게는 가능하다.
trip__to = ThailandPackage()
trip__to.detail()

from travel import vietnam
trip___to = vietnam.VietnamPackage()
trip___to.detail()

from travel import *  # travel의 모든것을 import 하겠다. 노출 범위를 정해줘야된다.
trip____to = vietnam.VietnamPackage()
trip____to.detail()
trip_____to = thailand.ThailandPackage()
trip_____to.detail()

# 잘 동작하는지 테스트를 해봐야 됨.

import inspect
import random
print(inspect.getabsfile(random))
print(inspect.getabsfile(thailand)) # 경로 탐색

