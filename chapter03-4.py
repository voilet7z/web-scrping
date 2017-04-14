from urllib.request import urlopen
from bs4 import  BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
    internalLInks = []
    for link in bsObj.findAll("a", href = re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLInks:
                internalLInks.append(link.attrs['href'])
    return internalLInks

def getExternalLInks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll("a",
                    href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return  addressParts

def getRandomExternalLinks(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html,'html.parser')
    externalLinks = getExternalLInks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getRandomExternalLinks(internalLinks[random.randint(0,
                                        len(internalLinks)-1)])
    else:
        return  externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLinks("http://oreilly.com")
    print("随机外链是:" + externalLink)
    followExternalOnly(externalLink)

allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html)
    internalLinks = getInternalLinks(bsObj.splitAddress(siteUrl)[0])
    externalLinks = getInternalLinks(bsObj.splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接："+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)


followExternalOnly("http://oreilly.com")
allIntLinks.add("http://oreilly.com")
getAllExternalLinks("http://oreilly.com")
