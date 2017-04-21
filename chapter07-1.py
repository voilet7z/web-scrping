from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def ngrams(content, n):
    content = re.sub("\n+", " ", content) #将多个换行符替换成空格
    content = re.sub(" +", " ",content)   #将多个空格替换成一个空格
    content = bytes(content, "utf-8")     #转换成utf-8格式，消除转义字符
    content = content.decode("ascii", "ignore")
    print(content)
    input = content.split(" ")
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html,"html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print("2-grams count is: "+str(len(ngrams)))