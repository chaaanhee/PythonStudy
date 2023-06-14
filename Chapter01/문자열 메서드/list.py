#list [] 안에 , 로 구분 / 배열
from types import DynamicClassAttribute


list_a = [1, 2, 3, 4]
list_b = ["a", "b", "c"]
list_c = [True, False]
list_d = [1, "a", False]
print(list_a)
print(list_b)
print(list_c)
print(list_d)

#list의 인덱싱과 슬라이싱
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
print(numbers[0])
print(numbers[3:5]) #list형으로 출력
print(numbers[1:])
print(numbers[-3:-1])

#문자열 안에서 문자만 출력
list_lan = ["JAVA", "C", "Python", "Go"]
print(list_lan[0][0])#J : 0번째 요소 중 0번째 글자 반환
print(list_lan[2][2:4])

#인덱싱을 활용하여 안에 내용 변경하기 / C를 C++로 변경
list_change = ["JAVA", "C", "Python", "Go"]
list_change[1] = "C++"
print(list_change)

#슬라이싱을 활용하여 내용 변경하기
#안에 내용이 늘어나거나, 줄어들 수 있다는 점 기억!
list_change[1:3] = ["C#", "Python#"] #마지막 요소는 들어가지 않으니 3으로 셋팅
print(list_change)

#len()
list_lang = ["JAVA", "C", "Python", "Go"]
print(len(list_lang))

#append() 리스트 맨 뒤에 제일 마지막 인덱스(-1)에 새로운 요소추가
print("append 요소")
list_lang.append("Rudy")
print(list_lang)
# 주의! 리스트를 추가 시 개별요소로 추가되는게 아니라 리스트 자체가 요소로 추가
#>>append가 아닌 extend 활용
list_a = [1, 2, 3]
list_lang.append(list_a)
print(list_lang)

#extend() 요소를 추가하는 방법
list_b = [4, 5, 6]
list_lang.extend(list_b)
print(list_lang)
# 주의! 문자 추가 시 단어 하나하나가 추가
list_lang.extend("Spring")
print(list_lang)

#insert(index, data) 원하는 위치<index>에 요소<data> 추가
list_lang.insert(0, "R")
print(list_lang)

#Pop(index) 요소반환
list_remove = ["JAVA", "C++", "Python", "Data"]
print(list_remove.pop(1))
print(list_remove)

#remove 해당 요소 삭제
list_remove.remove("Data")
print(list_remove)

#del 변수name[index] : 인덱스 위치에 있는 요소 삭제 
del list_remove[0]
print(list_remove)
