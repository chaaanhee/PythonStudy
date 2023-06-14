import requests
from bs4 import BeautifulSoup
r = requests.get("https://vibe.naver.com/chart/total")
bs = BeautifulSoup(r.text, "html.parser")

#가수의 목록
#노래의 목록
song_name = []
artist_name = []

song = bs.select("td.song > span.inner_cell > a.link_text")
print(song)
artist = bs.select("td.artist > a > span.text")
print(artist)