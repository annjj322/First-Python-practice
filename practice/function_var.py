def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print(f"이름 : {name}\t 나이 : {age}\t", end=" ")
    print(lang1,lang2,lang3,lang4,lang5)

profile("유재석", 20, "python", "java", "C", "C++", "C#") #하나 더배우면 함수를 바꿔야됨
profile("김태호", 25,"Kotlin","Swift","","","") # 없는사리를 빈자리라고 써줘야됨

# 이때 필요한게 가변인자.

def profile2(name, age, *language):
    print(f"이름 : {name}\t 나이 : {age}\t", end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile2("유재석", 20, "python", "java", "C", "C++", "C#", "java script")
profile2("김태호", 25,"Kotlin","Swift")


# 지역변수 , 전역변수
# 지역변수 - 함수가 끝나면 사라지는 변수

gun = 10

def checkpoint(soldiers) :
    global gun # This gun is a gun defined inside the function
    gun = gun - soldiers # This gun is a gun defined outside the function
    print(f"[함수 내] 남은 총 : {gun}")

def checkpoint_ret(gun, soldiers):
    gun = gun-soldiers
    print(f"[함수 내] 남은 총 : {gun}")
    return gun

print(f"전체 총 : {gun}")
checkpoint_ret(gun,2)
print(f"남은 총 : {gun}")