height = input("your height ")
gender = input("your gender ")

def std_weight(height, gender):
    if gender == "male" :
        weight = int(height)*int(height)*22/10000
        gender = "남자"
    if gender == "female" :
        weight = int(height)*int(height)*21/10000
        gender = "여자"
    weight = weight - weight % 0.01  #solution = round(weight,2)
    print(f"키 {height}cm {gender}의 평균 체중은 {weight}kg 입니다.")


std_weight(height,gender)