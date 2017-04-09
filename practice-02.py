import urllib
import urllib.request
import re
import time
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
def download_page(url):
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data

def get_image(html):
    regx = r'http://[\S]*\.jpg'
    pattern = re.compile(regx)
    get_img = re.findall(pattern, repr(html))
    num = 1
    for img in get_img:
        image = download_page(img)
        with open("%s.jpg"%num,'wb') as f:
            f.write(image)
            num += 1
            print("download%spiccture"%num)
            time.sleep(1)
    return

url = "http://www.tooopen.com/img/87.aspx"
html = download_page(url)
get_image(html)