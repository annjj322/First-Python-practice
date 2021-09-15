cabinet = {3:"유재석", 100:"김태호"} # key : value
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # program is over
print(cabinet.get(5)) # None
print(cabinet.get(5, "사용가능")) # if none-> 사용가능

print(3 in cabinet) # boolean

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])


# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력 
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 폐점
cabinet.clear()
print(cabinet)