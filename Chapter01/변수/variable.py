from tkinter import N


print("Hello, World!")

apple = '사과'
apples = '사과들'
apple3 = '사과3개'
app3le = '사3과'
red_apple = '빨간 사과'

print(red_apple) #스네이크케이스_밑줄 변수
print(app3le)

del (apple3)
#변수를 삭제하는 코드

# 잘못된 예시
# 숫자가 앞에 나오면 안됨.
# 3apple = '3개의 사과'
# apple! = '사과!'

a, b = 100, 200
a, b = b, a + b
# = 는 항상 마지막, +가 우선순위가 더 높다.
print(a, b)

text = "Hello, World~"
print((text + '\n') * 10)

name = '김찬희'
phone_num = '01065758157'
adress = '경기도 부천시'
print(name + '\n' + phone_num + '\n' + adress)

