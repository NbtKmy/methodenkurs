import requests
from bs4 import BeautifulSoup
import re

html = requests.get("https://warp.ndl.go.jp/info:ndljp/pid/11236451/www.kantei.go.jp/jp/kan/statement/201006/08kaiken.html")
html.raise_for_status()
soup = BeautifulSoup(html.text, "html.parser")


p_contents = soup.find_all("p")


kan_speech = ""

for i in p_contents:
	j = i.text
	if ("菅総理冒頭発言" in j) or ("(菅総理)" in j):
		kan_speech = kan_speech + j

a = kan_speech.replace('\n', '')
b = a.replace('\r', '')
c = b.replace('(菅総理)', '(菅総理)\n')
d = re.sub(r'\(内閣広報官\).*\(菅総理\)', '', c)
e = d.replace('【質疑応答】', '')
f = e.replace('(菅総理)\n', '')
g = f.replace('【菅総理冒頭発言】', '')
h = g.replace('\n', '')
z = h.replace('　', '')


with open('/home/nobu/Desktop/kan_pk.txt', mode='w') as f:
    f.write(z)

