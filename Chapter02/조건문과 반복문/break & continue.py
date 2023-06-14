#탈출문
#break : 반복문을 중단 >> 아래코드는 실행되지않음.
#continue : 반복문을 생략

i = 0
while True :
    print("{}번째 반복입니다.".format(i))
    i += 1
    if i > 10:
        break

#정수를 입력받아, 정수를 합계에 더하여 합계출력
sum_ = 0
while True :
    num = int(input("정수를 입력해주세요(0입력시 종료) >"))
    if num == 0:
        break
    sum_ += num
    print("정수의 합은 {}입니다.".format(sum_))

#continue : 생략 >> 아래 코드는 생략됨. 
#브레이크와 다른 점은 브레이크는 만나는 순간 코드종료지만, 컨티뉴는 만나는 순간 아래코드 생략 후 다시 반복실행
number = [10, 200, 30, 400, 50]
for j in number:
    if j < 100:
        continue
    print("{}은 100 이상의 숫자입니다.".format(j))


#중첩 for 문 탈출문
numbers = [[1,2,3],["가","나","다"]]
for e in numbers:# 2. 2번째 for 탈출 후 다시 돌아옴.
    print(e)     #
    for w in e : # 3. 리스트2의 첫번째 요소만 출력 후 다시 브레이크를 만나 종료 
        print(w) #
        break    # 1. 제일 가까운 for만 탈출
