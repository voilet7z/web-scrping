import json
import urllib.request

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

def getCountry(ipAddress):
    request = urllib.request.Request("http://antiquant.com:8080/json/"+ipAddress,headers=headers)
    response = urllib.request.urlopen(request).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

print(getCountry("105.215.85.74"))