#인덱스를 기반으로(순서를 기반으로) 값을 저장
#수정, 삭제, 추가 불가능
#but, 메모리 저장공간이 적고, 인덱싱 시간이 빠름

#list[] tuple()
numbers = (1, 2, 3, 4)
numbers02 = 1, 3, 5, 7
number = (9,) #마지막에 콤마를 넣어야 튜플
number02 = 0,
print(numbers)
print(type(numbers02))
print(type(number))
print(type(number02))

numberplus = (1, 2, 3)
#print(numberplus + 2) # inset... 사용불가
print(id(numberplus))

Nnumber = (1, 2, 3, (4, 5, 6))
print(Nnumber)
print(Nnumber[3]) #index

#언팩킹 : 안에 들어있는 요소들을 여러개의 변수에 대입하는 것
numbering = (1, 2, 3)
#number1 = numbering[0]
#number2 = numbering[1]
#number3 = numbering[2] //3줄을 1줄로 줄일 수 있음
number1, number2, number3 = numbering #요소의 갯수와 언팩킹 갯수와 맞지않으면 에러
print(number1, number2, number3)

#요소가 언팩킹수보다 많을 경우, 남은 요소를 담을 언팩킹 앞에 *를 붙여주기
packingEx = 1, 2, 3, 4, 5
packing1, packing2, *packing3 = packingEx
print(packing1, packing2, packing3)

#정말 추가할 수 없을까?
numberplus += 5, 6,
print(numberplus)
print(id(numberplus)) #메모리의 주소값이 위 값이랑 다름
#동일한 튜플이 아니라 요소를 추가한 새로운 튜플이라는 것 = 추가불가
