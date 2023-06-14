list_2nd = [[1, 2, 3], ["a", "b", "c"]]
for a in list_2nd :
    for b in a : #b 는 a 안의(in) 요소들을 출력 // print(list_2nd[a][b])=1 
        print(b)

for i in range(1, 3) :
    for j in range(1, 3):
        print("첫번째 for문의 반복 {}번, 두번째 for문의 반복 {}번".format(i, j))

#가장 가까운 for 문으로 돌아가기때문에, j의 for문으로 돌아감
# >>다시 i의 for 문으로 돌아가서 2를 할당함.        

#구구단 만들기
#2x1=2 2x2=4 2x3=6 ... 2x9=18
#..
#9x1=9 9x2=18 9x3=27...9x9=81
# 2단부터 9단까지 = 8번 반복
# 1부터 9까지 곱 = 9번 반복
print("구구단 만들기")
for g in range(2, 8+1):
    for y in range(1, 9+1):
        print(f"{g} x {y} = {g*y}", end = "\t")
    print() #end때문에 추가

#3중for문
print("3 for")
list_3rd = [[[1,2,3],[4,5,6]],[[11,23,45],[55,78,23]]]
for n in list_3rd:
    for x in n :
        for z in x :
            print(z)

list_4 = [[[1,2,3],[4,5,6]],[[11,23,45],[55,78,23]]]
cnt1 = 0
cnt2 = 0
cnt3 = 0
for p in list_4:
    cnt1 += 1
    #print("p의 {}번째 반복입니다.".format(cnt1))
    for o in p:
        cnt2 += 1
        #print("o의 {}번째 반복입니다.".format(cnt2))
        for u in o:
            cnt3 += 1
            #print("u의 {}번째 반복입니다.".format(cnt3))
            print(u) 
print("p는 {}번 반복, o는 {}번 반복, u는 {}번 반복".format(cnt1,cnt2,cnt3))