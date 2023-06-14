#변수와 함수를 갖고있는 코드
#클래스를 이용해 만든 객체를 인스턴스라고 한다.
from unicodedata import category

class BreadMold :
    #속성 == 일반적인 변수
    category = "크림빵"

#객체이름 = 클래스이름()
#클래스이름() >> 생성자

bread = BreadMold()
#객체의 고유만의 속성을 갖을 수 있다.
bread.price = 300
bread_choco = BreadMold()
bread_choco.category = "초코빵"

#문자열 뒤에 . == 참조연산자, 접근한다라고 생각 / ex).format()
print(bread.category)
print("{}의 가격은 {}입니다.".format(bread.category,bread.price))
print(bread_choco.category)

#클래스는 함수도 갖을 수 있다.
#클래스 내에 함수를 메서드라고 부른다. (일반적으로 참조연산자 사용)
class BreadMall :
    category = "단팥빵"
    def make_bread(self): #self : 변수없이 인자가 함수를 호출할때 파이썬은 암묵적으로 인자를 추가, 그래서 self라는 변수가 필요하다.
        print("빵을 만듭니다.")

bread = BreadMall()
bread.make_bread()       
