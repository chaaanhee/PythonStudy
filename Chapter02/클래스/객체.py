#int(), str(), float(), bool(), tuple()...type()
# 클래스

number = 1
#1이라는 데이터는 int의 인스턴스(객체)로 활용
text = "a"
print(type(number))
print(type(text))
a = 1
#id() = 객체의 주소값을 반환
#같은 주소값을 갖는다는 것은 같은 객체라는 의미
print(id(number))
print(id(a))
print(id(1))

#isinstance(number, int) == number라는 객체(isinstance)가 ,뒤 클래스(int)를 이용해서 만들어졌는지 확인
#True, False로 리턴
print(isinstance(number,int))