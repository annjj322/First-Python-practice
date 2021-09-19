# 서버에 접속되지 않는 현상
# 숫자값 대신 문자값을 입력했을 때 나타나는 현상

try: # try 내부의 입력된 문장은 잘 실행 되다가 에러가 발생하면 except값을 찾아서 실행
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
# nums.append(int(nums[0] / nums[1])) 이 없는 상태에서의 오류
except: # 나머지 모든 오류에 대해서 처리해준다. 정확한 오류내용은 Exception as err: 를 추가해주면 된다.
    print("알 수 없는 에러가 발생했습니다.")

# 의도적으로 발생시키는 오류
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10 :
        raise ValueError  # 의도적으로 에러를 발생시킨다.
    print("{0} / {1} = {2}". format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")