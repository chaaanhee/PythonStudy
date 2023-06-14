#뉴스 검색, 기사제목, 링크를 각 리스트에 담아서 출력
from operator import ne
import requests
from bs4 import BeautifulSoup
import pandas as panda

r = requests.get("https://news.google.com/search?q=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&hl=ko&gl=KR&ceid=KR%3Ako")
bs = BeautifulSoup(r.text, "html.parser")

#기사제목, 링크
titles = bs.select("div.xrnccd > article > h3 > a")
news = []
print(titles)
for i in titles:
    title = i.text
    links = "https://news.google.com" + i.get("href")[1:] #링크안에 .을 빼는 과정

    news.append([title,links])
    googleNeswDf = panda.DataFrame(news, columns=["기사제목", "링크주소"])

googleNeswDf.to_excel("뉴스크롤링 결과.xlsx")
print("저장성공")