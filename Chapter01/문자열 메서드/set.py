#순서가 정해져있지 않고, 중복을 허용하지 않음
week = {"월요일", "화요일", "수요일", "목요일", "월요일"}
print(week)

#add = 숫자, 문자, True, ("튜플")은 추가가능
#[1,2,3]리스트, {keys:valus}딕션어리는 불가능
week.add("화요일")
print(week)

#FALSE와 0 / True와 1은 같이 사용할 수 없음
a = {2, "abc", False}
a.add(3)
print(a)

#week.add(("일주일",)) #튜플의 형태로 추가
#print(week)
week.update(("일주일",)) #튜플 안 요소가 요소자체로 추가
print(week)
week.update(["일주일"],{"한달":123}) #키값만 추가
print(week)

#리스트나 튜플같은 시퀀스 자료형을 집합으로 변환하고 싶을 때, 사용
#중복원소가 사라지는 건 유용하나, 순서는 엉망진창
week = set(["월요일", "화요일", "수요일", "토요일", "일요일", "수요일"])
print(week)

b = {1, 3, 5, 7}
c = {1, 2, 3, 4, 5}
#합집합 (중복을 허용하지않음)
print(b | c)
#교집합
print(b & c)
#차집합
print(b - c)
#원소삭제
b.remove(3)
b.remove(True) #1이 지워짐. false일 경우에는 0이 지워짐
print(b)