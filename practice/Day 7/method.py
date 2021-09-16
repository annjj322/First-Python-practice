# 일반 유닛
class Unit: # 부모 class
    def __init__(self, name, hp, speed):
        self.name = name  # 일반 유닛과 공격 유닛에서 공통적으로 있는 사항 = 상속을 사용
        self.hp = hp   
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
       
# 공격 유닛
class AttackUnit(Unit): # Unit을 상속받아서 만들어 진 것. 자식 class
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location,):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}][속도 ({3})]".format(self.name, location, self.damage, self.speed))


    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp<= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 메딕 : 의무병 (공격력이 없는것이 특징)

# 드랍쉽 : 공중 유닛, 수송기 (공격 X)
class Flyable:
    def __init__(self, flying_speed): # name에 대한 요소가 없다.
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name,location,self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중 상속을 받아서 초기화해준것.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # flying_speed가 있기 때문에 speed는 필요 없다. 지상 스피드 == 0 이라는 뜻
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")  # 공중 유닛은 fly, 지상 유닛은 move를 쓰는 것이 매우 귀찮음. 그렇기에 메소드 오버라이딩을 해야함



# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6,5)
valkyrie.fly(valkyrie.name, "3시") # Flyable 에 name 요소가 없고, fly 함수에 name요소가 있기때문에 이름도 적어야 됨.              

firebat1 = AttackUnit("파이어뱃", 50, 3, 16)
firebat1.attack("5시")

# 공격을 두번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
