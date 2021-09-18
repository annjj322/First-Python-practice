class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))
        # 정의되어 있는 요소만 print 하는 경우에 사용하는 format = 그냥 나열한다.

# solution = gang, ma, song 을 사용하지 않고 바로 넣어서 해도 된다.

gang = House("강남","아파트","매매","10억","2010년")
ma = House("마포","오피스텔","전세","5억","2007년")
song = House("송파","빌라","월세","500/50","2000년")

house = []
house.append(gang)
house.append(ma)
house.append(song)

print("총 3대의 매물이 있습니다.")
# print("총 {0}대의 매물이 있습니다.".format(len(house)))


for i in house:
    i.show_detail()


# houses = []
# house1 = House("강남","아파트","매매","10억","2010년")
# house2 = House("마포","오피스텔","전세","5억","2007년")
# house3 = House("송파","빌라","월세","500/50","2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)
