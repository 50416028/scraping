import requests
from bs4 import BeautifulSoup

r = requests.get("https://news.yahoo.co.jp/")

#第一引数:解析したいもの, 第二引数:何を元に解析するか(htmlなのでhtml.parser)
soup = BeautifulSoup(r.content,"html.parser")

#ニュース一覧のテキストのみ抽出
print(soup.find("ul","newsFeed_list").text)
