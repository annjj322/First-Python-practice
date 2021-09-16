# __init__ = 생성자. (객체: 클래스로부터 만들어지는 애)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp   
        self.damage = damage  
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력{self.damage}")

marine1 = Unit("마린") # 실행되지 않음. __init__뒤의 공간개수만큼 채워줘야됨.

