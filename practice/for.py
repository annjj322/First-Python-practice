print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [0,1,2,3,4] :
    print(f"대기번호 : {waiting_no}")

for wating_nom in range(1,6): # 순차적인 수
    print(f"대기번호 : {wating_nom}")

starbucks = ["iron_man", "thor", "groot"]
for customer in starbucks:
    print(f"{customer}, coffee is ready")