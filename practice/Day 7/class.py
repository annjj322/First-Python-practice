# marine : 공격 유닛, 군인, 총을 쏠 수 있음
name = "marine"
hp = 40
damage = 5

print(f"{name} 유닛이 생성되었습니다.\n체력 {hp}, 공격력 {damage}\n")

# tank : 공격 유닛, 일반모드/시즈모드
tank_name = "tank"
tank_hp = 150
tank_damage = 35

print(f"{tank_name} 유닛이 생성되었습니다.\n체력 {tank_hp}, 공격력 {tank_damage}\n")

tank2_name = "tank2"
tank2_hp = 150
tank2_damage = 35

print(f"{tank2_name} 유닛이 생성되었습니다.\n체력 {tank2_hp}, 공격력 {tank2_damage}\n")

def attack(name, location, damage):
    print(f"{name} : {location} 방향으로 적군을 공격 합니다. [공격력 {damage}]")

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage) # 실제 게임에서는 수십에서 수백개의 유닛이 존재.

# class = 붕어빵 틀

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp   
        self.damage = damage  
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력{self.damage}")

marine1 = Unit("마린", 40, 5) # 결론적으로 실행하게 해주는 코드 마린이라는 유닛의 이름, 체력, 공격력
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}") # 일반 출력문으로 부가설명만 하는 것.

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))