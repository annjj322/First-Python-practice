from random import randrange, shuffle
customer = list(range(1,51))
sum_customer = 0
for i in customer:
    random_time = list(range(5,51))
    shuffle(random_time)
    random_time = random_time[0]
    if 5<= random_time <=15:
        user = "O"
        sum_customer += 1
    else:
        user = ""
    print(f"[{user}] {i}번째 손님 (소요시간 : {random_time})")
print(f"총 탑승 승객 : {sum_customer}분")



# solution
cnt = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print(f"[0] {i}번째 손님 (소요시간 : {time}분)")
        cnt += 1
    else:
        print(f"[] {i}번째 손님 (소요시간 : {time}분)")

print(f"총 탑승 승객 : {cnt} 분")