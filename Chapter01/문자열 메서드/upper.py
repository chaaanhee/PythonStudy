from dataclasses import replace
from pydoc import stripid

text = "www.GOOGLE.com"

#len() 문자열의 길이를 반환, 내장함수 length의 약자, 요소값의 갯수
print(len(text)) #문자갯수

#capitalize() 캐피탈라이즈 : 문자열에서 가장 첫번째 글자를 대문자로 변경
#.(참조연산자)오른쪽기능이 왼쪽값에 적용됨
txt_cap = text.capitalize()
print(txt_cap)

txt_up = text.upper()#upper() 문자열 전체를 대문자로 변경
txt_lower = text.lower()#lower() 문자열 전체를 소문자로 변경
print(txt_up)
print(txt_lower)

g_cnt = text.count('G')#찾는 문자의 갯수 반환, G가 몇번 발생했는가, 없으면 0 반환
g_find = text.find('G')#찾는문자의 index를 반환, index는 0번부터 시작
g_find5 = text.find('G', 5 )#5번 index부터 시작되는 문자 중 G의 index반환
g_idx = text.index('G')#찾는 문자의 index 반환 
print(g_cnt) #2
print(g_find) #4
print(g_find5) #7
print(g_idx) #4

#find와 index의 차이점을 제일 크게 느낄 수 있을 땐, 문자열에 해당문자가 없을때
x_find = text.find('x') #해당 문자가 있는지 없는지 확인하고싶을때 추천
#x_idx = text.index('X')
print(x_find) #-1
#print(x_idx) #에러

g_rfind = text.rfind('G') #보통 왼쪽>오른 방향이지만, r을 붙이면 오른>왼 방향으로 찾음
print(g_rfind) #7

txt_naver = text.replace("GOOGLE", "NAVER") #문자열 치환, 앞의 값을 뒤의 값으로 치환
print(txt_naver)

#split : 문자열을 분리해주는 메서드
print(text.split('.')) #,로 구분 / .이 기준으로 구분되어짐
print(text.split('OO')) #넣은 값은 사라짐

#strip 좌우공백을 메꿔주는 메서드
text_Na = "     www.NAVER.com       "
text_Nav = "w w w . N A V E R . C O M"
stp = text_Na.strip()
print(text_Na)
print(text_Nav)#글자 사이에 있는 공백은 적용X
print(stp)