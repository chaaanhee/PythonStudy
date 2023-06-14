weather = "맑음"
temperature = 20
chance_shower = 33.5
#문자데이터타입:s / 숫자(정수)데이터타입:d / 숫자(소수)데이터타입:f

##percent sign(%)
#d는 정수 , f는 소수
print("오늘의 날씨는 %s 기온은 %d도 비가 내릴 확률은 %.1f%%입니다."%(weather, temperature, chance_shower))

##format
print("오늘의 날씨는 {} 기온은 {}도 비가 내릴 확률은 {}입니다.".format(weather, temperature, chance_shower))
print("오늘의 날씨는 {0} 기온은 {1}도 비가 내릴 확률은 {2}입니다.".format(weather, temperature, chance_shower))
#중괄호의 숫자가 요소보다 많으면 에러발생
print("{:10},{:10}".format(weather,temperature))
#문자는 왼쪽정렬, 숫자는 오른쪽정렬

#데이터타입
print("{0:s},{1:d},{1:.1f},{1:o},{1:x}".format(weather,temperature))
#d는 10진수 / o는 8진수 / x는 16진수

#정렬은 <>^ 으로 지정가능
left = "left"
right = "right"
center = "center"
print("({:<10s}),({:^10s}),({:>10s}),".format(left,center,right))
print("({2:>10s}),({1:^10s}),({0:<10s}),".format(left,center,right))
print("({2:#>10s}),({1:@^10s}),({0:!<10s}),".format(left,center,right))
print("({2:#>10.3s}),({1:@^10.4s}),({0:!<10.2s}),".format(left,center,right))

##f-string
print(f"오늘의 날씨는 {weather}이며, 기온은 {temperature}입니다.")
print(f"2 곱하기 60의 결과값은 {2*60}입니다.")