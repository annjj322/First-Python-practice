# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"} #set
print(menu, type(menu))

menu = list(menu) #list
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))