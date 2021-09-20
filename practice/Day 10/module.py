# 현금만 받는 극장, 잔돈을 바꿔주지 않음.
import theater_module # 확장자 생략
theater_module.price(3) # 3명이서 영화를 보러 갔을 때의 가격
theater_module.price_morning(4) # 4명이서 조조할인 영화를 보러 갔을 때의 가격
theater_module.price_soldier(5) # 5명의 군인이 영화를 보러 갔을 때의 가격

import theater_module as mv # 별명을 붙여줘서 줄일 수 있다.
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
price(3)
price_soldier(5)
price_morning(4)

from theater_module import price, price_morning
price(5)
price_morning(6)
price_soldier(4) # 오류가 날 것이다.

from theater_module import price_soldier as ps
ps(5)