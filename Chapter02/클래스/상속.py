#상위-하위클래스 (Inheritance)
#super 부모클래스
#sub 자식클래스
#자식클래스 확인하는법
#issubclass(자식클래스, 부모클래스) == 자식클래스는 부모클래스의 하위클래스다. >> 불린형으로 반환
class ParentRestaurant: 
    price = 13000
    def __init__ (self, name, menu, recipe):
        self.name = name
        self.menu = menu
        self.recipe = recipe

    def __str__(self):
        return "가게 이름 :{}, 가게 메뉴 :{}, 가게 레시피 :{}".format(self.name, self.menu, self.recipe)

    def __del__(self):
        pass

#상속 : class 자식클래스(부모클래스):
class ChildRestaurant (ParentRestaurant):
    price = 14000 #overriding : 재정의
    marketing = "온라인 마케팅" #추가한 것 뿐, 재정의(오버라이딩)는 아니다.
    def __init__(self, name, menu, recipe, reservation):
        ParentRestaurant.__init__(self, name, menu, recipe)
        self.reservation = reservation

    def __str__(self):
        return super().__str__() + ", 예약 : {}".format(self.reservation)    

restaurant_info = ChildRestaurant("요리고토", "고등어구이", "머랭치기", "가능")
#print(restaurant_info.marketing) 
print(restaurant_info) 

print(issubclass(ChildRestaurant,ParentRestaurant))