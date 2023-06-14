#__init__ 생성자 메서드 : 초기화(초기값을 넣어준다.)의 뜻을 갖고있다.
#initialize의 약자
#__del__ 소멸자 메서드 : 객체가 소멸이 될 때, 호출되는 메서드
# bread1[객체변수>>객체를 가져다 쓰는 이름] = BreadMold() 
class BreadMold :
    category = "빵"
    def __init__(self, category ,price) :
        self.category = category
        self.price = price
        print("빵을 만듭니다.")
    
    def __str__(self) :
        return "{}의 가격은 {}원 입니다".format(bread1.category, bread1.price)
        
    def __del__(self):
        print("빵이 없어졌습니다.")

bread1 = BreadMold("단팥빵", 3000)

#생성해준 인스턴스마다 각 속성의 값이 달라야한다면, 인스턴스의 속성으로 넣어주는게 맞다 
#위 경우 __init__ 생성자 메서드를 추천
#print("{}의 가격은 {}원 입니다".format(bread1.category, bread1.price))

#__del__
#참조하고 있던 객체의 변수들이 더이상 참조하고 있지 않을 때 실행(=레퍼런스카운터)
# 레퍼런스카운터가 0이 되면 소멸자 메서드가 호출된다 

#변수는 객체가 X아니다.
#변수는 객체를 가르키고 있는 단순한 이름표일뿐!

#__str__ 객체가 문자열로 반환될때, 출력값을 지정해줄 수 있다.
#지정을 안했을 시엔 init와 del 사이에 데이터 위치를 알 수 있는 문구가 출력된다.
