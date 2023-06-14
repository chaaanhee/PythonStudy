# 변수 = {"키keys":"값values"}
# 키를 기반으로 값을 저장
#키와 값이 쌍을 이루는 자료구조
people ={
    "name":"김찬미",
    "phone":"010-333-3333"
    }
print(people["name"], people["phone"])

books = {"Daniel Pink":["파는 것이 인간이다.","언제 할 것인가"],
        "Eric Shidt":"새로운 디지털 시대"
 }
print(books["Daniel Pink"], books["Eric Shidt"])

#키 값이 True(논리형)일 경우 숫자 1과 같은 값, false는 정수 0과 같은 값   
book = {3 : "쓰리", True : "True"}
print(book[3])

#추가
coffee = {"JAVA":2500, "Americano":3500, "Latte":5000}
coffee["MOCA"] = 4000
#print(coffee["JAVA"])
print(coffee)

#삭제
del coffee["JAVA"]
print(coffee)
coffee.pop("MOCA")
print(coffee)

#찾기
print(coffee["Americano"])
print(coffee.get("Latte"))
print(coffee.keys()) 
print(coffee.values())

#키와 값을 튜플로 반환
print(coffee.items())

#확인
print("Latte" in coffee)
print("ICE Latte" not in coffee)

