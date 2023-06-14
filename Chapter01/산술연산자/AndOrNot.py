# and : 모두 참일 경우 참
print(True and True)
print(True and False)
print(10>3 and 3<5)
print(10==1 and 1==5)

#or : 하나만 참이여도 참, 모두 거짓일 경우에만 거짓
print(True or True)
print(False or True)
print(False or False)

#and
print("a" and 10>3 and 0)#거짓으로 판별되는 1번째 값이 나옴
print("a" and 10>3 and True and "참")#모든값이 참일경우 마지막 참이 결과값

#or 
print(0 or 0.0 or False or "a")#참으로 판별되는 1번째 값이 나옴
print(0 or 0.0 or False or "")#마지막 거짓이 결과값

#and > or
print(True or False and "참") #True >> and연산이 or보다 높음
print((True or False) and "참")

#not : 참을 거짓으로, 거짓을 참으로 뒤집어주는 역할
print(not (True or False))
print(not True)

