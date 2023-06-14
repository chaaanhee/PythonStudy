#while 조건식 :
#   조건식이 참일동안 실행할 문장
i =0
num = 10
while i < num :
    i = i + 1
    print(i)
else :
    print("값이 {}이상이므로 종료합니다.".format(num))

number = 1
while number <= 5 : ##1값이 제일 먼저만나는 건 조건식 → 바로 실행문을 만나서 2부터 출력
    number += 1
    print(number)
else :
    print("number의 마지막값은 {}입니다.".format(number))

#1부터 5까지만 출력
number2 = 1
while number2 <= 5:
    print(number2)
    number2 += 1    

#if문은 조건식이 참일경우 한번만 실행
#if i < num :
#    i = i + 1
#    print(i)

fruits = ["사과", "키위", "바나나", "사과", "바나나", "망고"]
fruit = input("삭제할 과일을 입력해주세요")
while fruit in fruits :
    fruits.remove(fruit)
#중괄호가 없는대신, 공백으로 들어가고 나가고를 결정하기에 공백 4칸이 중요
print(fruits)
print("{}를 모두 제거했습니다.".format(fruit))
