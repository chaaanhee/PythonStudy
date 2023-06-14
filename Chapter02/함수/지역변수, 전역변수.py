#지역변수(Local Variable)
#전역변수(Global Variable)

def jeju_potato(): #(popo) 매개변수도 지역변수
    potato = "고구마" #지역변수는 함수내에서만 사용할 수 있다 / 함수가 종료되면 지역변수 삭제
    print(potato)
jeju_potato()
#print(potato) >> 에러발생

tomato = "토마토"
def jeju_tomato():
    print(tomato)

jeju_tomato()
print(tomato)

#함수 내부에 있는 키워드를 전역변수로 사용하고 싶다면, global 함수사용
apple = "사과"
def jeju_apple():
    global apple
    print(apple) # 우선순위가 local > global 이라 글로벌이 없었으면 에러발생
    apple = "딸기"
    print(apple)
jeju_apple()