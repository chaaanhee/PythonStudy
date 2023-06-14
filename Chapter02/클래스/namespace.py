#Namespace = 클래스의 이름공간
#무언가를 찾을 때 우선순위
# 객체의 이름공간 > 클래스 이름공간 > 전역변수 
# dir() 이름 공간에 있는 모든 속성을 리스트로 반환 
from unicodedata import category

class BreadMold :
    category = "빵"

bread1 = BreadMold()
bread2 = BreadMold()
bread3 = BreadMold()

#객체의 속성을 재할당
bread2.category = "붕어빵" 
bread3.category = "잉어빵"
#속성을 추가(다른객체들에 영향을 끼치지 않음)
bread1.price = 3000

print(bread1.category, bread2.category, bread3.category)
print(dir(bread1))
print(dir(bread2)) #1에 추가한 속성은 포함되어있지 않음.
print(dir(BreadMold))