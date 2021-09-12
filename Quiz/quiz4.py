# 댓글 20명, 아이디는 1~20이라고 가정
# 무작위 추첨, 중복 불가
# RANDOM의 SHUFFLE , SAMPLE 이용

from itertools import starmap
from random import *
 
lst = list(range(1,21))
shuffle(lst)
chicken = list(sample(lst,1))
cof_set = list(set(lst)-set(chicken))
coffee = sample(cof_set,3)


print(f"-- 당첨자 발표 -- \n 치킨 당첨자 : {chicken}\n 커피 당첨자 : {coffee}\n -- 축하합니다 --")