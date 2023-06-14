import module as M
#from module import add as A
#from module import add, sub

M.add(10,2)
M.sub(4,9)
M.mul(9,2)
M.dev(100,2) #나눗셈 연산자는 항상 실수형으로 반환

#파이썬이 갖고있는 모듈
from datetime import date, time, datetime, timedelta
today = date.today()
print(today)
new_date = date(1994, 8, 22)
print(new_date)

print(time(9)) #시단위
print(time(9, 2)) #분단위
print(time(9, 2, 2)) #초단위
print(time(9, 2, 2, 2)) #m초단위

dt = datetime.now() #현재날짜, 시깐까지
print(dt)
dtt = datetime(1994, 8, 22, 11, 10, 45)
print(dtt)

#연산자 timedelta(days = 숫자, hours =, weeks =, minutes=) : 날짜를 빼거나 더할 수 있다.
today = datetime.now()
print(today)
print(today - timedelta(days = 20))

#import time
#간단하게 현재 시간을 알려줄 수 있는 모듈
#datetime의 time과 이 time은 전혀다름
#1977년 1월 1일 0시 0분 0초부터 지금까지의 경과한 모든 시간을 초단위로 반환
#now = time.time()
#print(now)

from time import localtime, strftime
#현재시간
now = localtime()
print(now)

#strftime = str(문자)f(포매팅) >> 날짜와 시간을 문자로 포매팅할 수 있는 함수
#now = strftime(%Y년%M월%a일 %H시%M분 )
print(now)

