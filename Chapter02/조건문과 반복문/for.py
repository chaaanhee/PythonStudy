for i in range(1, 10+1) :
	print(i)

#문자열
for j in "일이삼사오" :
    print(j)

#리스트
fruits = ["사과", "딸기", "바나나"]
for r in fruits :
    #print(r)
    print("과일바구니에 {}가 들어있습니다.".format(r))

#1부터 30까지의 수 중에서 3의 배수들의 합을 구하시오.
#3의 배수 % 3 == 0
sum = 0
for i in range(1, 30+1) :
    if i % 3 == 0:
        print("{} + {} =".format(sum, i), end = "")
        sum += i #1번째 출력 후 sum이 3이 된다.
print(sum)

#step을 사용하면 if문을 사용하지 않아도 된다.
summ = 0
for k in range(3, 30+1, 3) : #시작을 3으로 시작!!
    print("{} + {} =".format(summ, k), end = "")
    summ += k 
print(summ)

#딕셔너리를 사용하여 for문
#.keys() : 딕셔너리 안 키 값만 반환
#.valuse() : 딕셔너리 안 벨류값만 반환
coffee = {"아메리카노":300, "라떼":500, "모카":600}
for c in coffee.items(): #items를 이용하면 딕셔너리 안에 키 값과 벨류값 모두 반환 가능
    print(c) #튜플의 형태로 반환

#enumerate : (인덱스번호, 리스트 안의 요소)를 하나씩 출력
#인덱스와 함께 사용할때 유용
sports = {"피구", "농구", "축구"}
for s in enumerate(sports):
    #print(s)
    print(f"{s[0]+1}번째 스포츠는 {s[1]}입니다.")