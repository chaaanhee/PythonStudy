#reguests
#pip3 install requests
import requests
#get : 자원을 요청 /<Response [200]>을 받으면 OK
print(requests.get("https://www.naver.com"))

r = requests.get("https://www.naver.com")
print(r.content) #정보를 요청한 것을 16비트로 변환
#print(r.text) #html 구조로 반환

#BeautifulSoup => python이 이해할 수 있도록 파싱을 사용
from bs4 import BeautifulSoup
bs = BeautifulSoup(r.content, "html.parser")
#h3 = bs.select("h3") #select : 인자로 입력한 요소를 전부 다 선택을 해준다. // 결과값이 여러개이기에 리스트형으로 반환
h3 = bs.select_one("h3") #select_one : "h3"요소 중에서 가장 앞에 있는 요소를 선택해주는 것
#print(h3.text) #<h3>안에 있는 텍스트만 뽑아내는 것, select_one 으로 지정하던가 인덱스를 지정해준다=> print(h3[1].text)
#print(h3.name) #태그의 이름
#print(h3.attrs) #class 정보
h3 = bs.select_one("h3 > a")#h3 안에 자식요소를 반환
#selecter = bs.select(".title") class속성을 선택할 때
#selecter = bs.select("#u_skip") id속성을 선택할 때
selecter = bs.select_one("div.current_box") #특정 class속성을 선택할 때
selecter = bs.find_all("div",{"class":"partner_box"}) #bs.find_all("태그명", {"속성명":"값"}) 자식요소선택
print(selecter)