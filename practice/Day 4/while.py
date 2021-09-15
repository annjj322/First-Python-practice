customer = "thor"
index = 5
while index>=1:
    print(f"{customer}, coffee is ready. {index} times left")
    index -=1 # index = index - 1
    if index == 0:
        print("coffee is gone")


#customer2 = "iron_man"
#index = 1
#while True:
#    print(f"{customer}, coffee is ready") # infinite loop
#    break

customer3 = "thor"
person = "Unknown"

while person != customer3 : # 조건에 만족할때까지 반복
    print(f"{customer3}, coffee is ready")
    person = input("What's your name?")