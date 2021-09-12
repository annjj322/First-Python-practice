absent = [2,5] #absent
no_book = [8] 
for student in range(1,11): # 1~10
    if student in absent:
        continue
    elif student in no_book:
        print(f"today's class is over. {student}! follow me")
        break
    print(f"{student}, please read a book")