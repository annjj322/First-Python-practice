def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance + money} 원입니다.")
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print(f"출금이 완료되었습니다. 잔액은 {balance-money} 원입니다")
        return balance-money
    else:
        print(f"잔액이 부족합니다. 잔액은 {balance} 원입니다")
        return balance

def withdraw_night(balance, money): # 저녁 출금 수수료 100원
    commission = 100
    return commission, balance - money - commission # 수수료와 출금+수수료를 빼고 남은 잔액 반환

balance = 0
balance =deposit(0,1000)
balance = withdraw(balance, 20000) # 잔액 초과
commission, balance = withdraw_night(balance, 500)
print(f"수수료는 {commission}원 이며, 잔액은 {balance}원 입니다")