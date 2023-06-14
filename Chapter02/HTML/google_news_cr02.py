#웹페이지에 들어가지 않고 뉴스 검색, 기사제목, 링크, 본문, 게시날짜를 엑셀에 담아서 출력
from operator import ne
import requests
from bs4 import BeautifulSoup
import pandas as panda
keyword = input ("검색하고자 하는 키워드를 입력해주세요 >")
r = requests.get("https://news.google.com/search?q="+ keyword +"&hl=ko&gl=KR&ceid=KR%3Ako")
bs = BeautifulSoup(r.text, "html.parser")

#기사제목, 링크

titles = bs.find_all("div",{"class":"xrnccd"})
news = []

for i in titles:
    title = i.find("h3").text
    links = "https://news.google.com" + i.find("a")["href"][1:] #링크안에 .을 빼는 과정
    #desc = i.find("span",{"class":"xBbh9"}).text
    data = i.find("time").text

    news.append([title, links, data])
    googleNeswDf = panda.DataFrame(news, columns=["기사제목", "링크주소", "개시날짜"])
print(titles)
googleNeswDf.to_excel("뉴스크롤링 결과2.xlsx")
print("저장성공")