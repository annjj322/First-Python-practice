print("Python", "Java", sep=",", end="?") # sep = fill the intervening space. end = fill the last space
print("무엇이 더 재밌을까요?")


import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)


# 시험 성적
scores = {"math":0, "English":50, "coding":100}
for subject, score in scores.items():
    #print(subject,score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")


# 은행 순번표
for num in range(1,21):
    print(f"대기번호 : {str(num).zfill(3)}")

answer = input("아무 값이나 입력하세요 : ") # input = always save it as str
print(type(answer))
print(f"입력하신 값은 {answer}입니다") 