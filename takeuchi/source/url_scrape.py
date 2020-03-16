import requests
import re

from bs4 import BeautifulSoup

r = requests.get("https://www.pixiv.net/ranking.php?mode=daily")
path = "../data/artworks.txt"

#出力が絶対パスの場合はコメント後で消す。
head = "https://www.pixiv.net"

#第一引数:解析したいもの, 第二引数:何を元に解析するか(htmlなのでhtml.parser)
soup = BeautifulSoup(r.content,"html.parser")

#htmlファイル中のurlの情報を全て抽出
links = [url.get('href') for url in soup.find_all('a')]

#"artworks"を含むurlを抽出
links_in = [s for s in links if 'artworks' in s]

#artworks.txtにurlを一行ずつ記入
with open(path,'wt') as f:
	for ele in links_in[::2]:
		f.write(head+ele+'\n')

