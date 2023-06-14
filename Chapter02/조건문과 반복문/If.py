#if True(조건식) : print...(조건식이 참일경우 실행할 문장)
#조건식 : 참과 거짓으로 판별될 수 있는 조건식
#실행문 앞에 공백 : 무조건 ✨4칸, 3칸으로 되면 에러 발생
if True :
    print("실행할 문장입니다")

weather = "비"
if weather == "비":
    print("우산을 챙겨주세요.")

#만약에 오늘 공부한 시간이 3시간 이상이라면 Good! 출력
#6시간 이하라면 Good!
#and : 둘 다 참이여야 함
study_time = int(input("오늘 공부한 시간을 입력해주세요."))
if study_time >= 3 and 6 >= study_time:
    print("Good!")

if 6 >= study_time >= 3:
    print("Good Good!")

#or : 둘 중 하나만 참이여도 참
Play_time = int(input("오늘 놀 시간을 입력해주세요"))
if Play_time < 3 or Play_time > 9 :
    print("공부해 어서!")

