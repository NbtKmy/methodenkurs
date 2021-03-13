from bs4 import BeautifulSoup
import re


def xmlParse():

    with open('reut2-002.xml') as f:
        s = f.read()

    soup = BeautifulSoup(s, 'lxml-xml')


    contents = soup.find_all("BODY")
    print(contents)

    news = ""

    for i in contents:
	    j = i.text
	    news += j




    with open('./news1987.txt', mode='w') as f:
        f.write(news)

if __name__ == "__main__":
    xmlParse()