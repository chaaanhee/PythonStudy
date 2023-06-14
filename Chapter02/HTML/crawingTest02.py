import re
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.takjakim.kr/macos/pip_install")
bs = BeautifulSoup(r.content,"html.parser")

pip3ins = bs.select_one("div.CodeBlock_container__3oY8L > div.CodeBlock_code__3am13 > span.token operator")
print("내가 찾는 코드는 {}입니다.".format(pip3ins.text))