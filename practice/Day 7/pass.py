class Unit: 
    def __init__(self, name, hp, speed):
        self.name = name 
        self.hp = hp   
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp<= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
       
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location,):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}][속도 ({3})]".format(self.name, location, self.damage, self.speed))


# 마린

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
    

# 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 본인의 체력을 10 소모
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
# 시즈모드 : 탱크를 고정시켜 세게공격, 이동불가.
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 시즈모드가 개발이 됐지만 시즈모드가 아닐때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *=2
            self.seize_mode = True
        # 시즈모드가 개발이 됐고 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /=2
            self.seize_mode = False

 
class Flyable:
    def __init__(self, flying_speed): 
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name,location,self.flying_speed))

 
class FlyableAttackUnit(AttackUnit, Flyable): 
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 일단은 완성된 것처럼 여겨지는 것. 일단 넘어감.

# 서플라이 디폿 : 건물, 1개 건물 = 8개 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # pass 

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over(): # pass 함수가 실행되지 X
    pass

game_start()
game_over()