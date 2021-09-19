class SoldOutError(Exception):
# solution
#    pass
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg



try: # 밖에 위치하기 때문에 에러가 발생하면 경고문과 함께 실행이 종료되어 버린다.
    chicken = 10
    waiting = 1
    while(True):
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1:
            raise ValueError
        elif order > chicken:
            print("재료가 부족합니다")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting,order))
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
            break # try의 위치때문에 SoldOutError에 break를 넣으면 에러가 발생
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except SoldOutError as err:
    print(err)


#chicken = 10
#waiting = 1
#
#while(True):
#    try:
#       print("[남은 치킨 : {0}]".format(chicken))
#       order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#       if order > chicken:
#           print("재료가 부족합니다")
#       elif order <= 0:
#           raise ValueError
#       else:
#           print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting,order))
#           waiting += 1
#           chicken -= order
#
#       if chicken == 0:
#           raise SoldOutError
#    except ValueError:
#        print("잘못된 값을 입력하였습니다.")
#    except SoldOutError:
#        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#        break