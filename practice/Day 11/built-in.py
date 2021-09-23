# input : 사용자의 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print(f"{language}는 좋은 언어입니다")

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수
print(dir())
import pickle
print(dir())

print(dir(random)) # random 내에서 쓸수 있는 것들 표시
lst = [1,2,3]
print(dir(lst))

name = "Jim"
print(dir(name))

# 더 많은 내장함수는 Built-in Functions --- Python 에서 찾아서 쓸 수있다.