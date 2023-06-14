from re import A

#리스트의 정렬
#숫자, 알파벳, 한글 모두 가능

#sort() : 오름차순으로 정렬(오른>왼 방향으로, 작>큰 숫자정렬)
numbers = [100, 20, 60, 4, 70, 3600]
#numbers.sort() 
print(numbers)

#reverse() : (바로 위)리스트 안에 있는 요소를 역순으로 변경
numbers.reverse()
print(numbers)

#sort(reverse = True) : 내림차순으로 정렬
numbers.sort(reverse=True) 
print(numbers)

#문자열(한글)
names = ["김찬희", "윤아영", "박하나"]
#names.sort() 자음의 순서대로 정렬
#names.sort(reverse=True) 자음의 역순으로 정렬
print(names)

#문자열(알파벳)
Fruit = ["banana", "apple", "watermelon"]
#Fruit.sort() 알파벳의 순서대로 정렬
Fruit.sort(reverse=True) #알파벳의 역순으로 정렬
print(Fruit)


#in 연산자와 not in 연산자
#in : 내가 찾는 값이 있으면 True, 없다면 False 반환
print(20 in numbers)
print("w" in Fruit)
print("apple" in Fruit)

#not in : in의 반대
print(20 not in numbers)
print("w" not in Fruit)
print("apple" not in Fruit)