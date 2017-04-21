from urllib.request import *
from bs4 import BeautifulSoup
import datetime
import re
import random
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                            href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is:"+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

#links = getLinks("/wiki/Python_(programming_language)")

#while(len(links)>0):
#   for link in links:
#        print("----------------")
#        historyIPs = getHistoryIPs(link.attrs['href'])
#        for historyIP in historyIPs:
#            print(historyIP)
#    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
#    links = getLinks(newLink)

def getCountry(ipAddress):
    try:
        request = Request("http://antiquant.com:8080/json/"+ipAddress,headers=headers)
        response = urlopen(request).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")

links = getLinks("/wiki/Python_(programming_language)")

while(len(links)>0):
    for link in links:
        print("----------------")
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+" is from "+country)

    newLink = links[random.randint(0,len(links)-1)].attrs['href']
    links = getLinks(newLink)