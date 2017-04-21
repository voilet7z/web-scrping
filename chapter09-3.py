import requests

files = {"uploadFile": open("../files/python-logo.png", "rb")}
r = requests.post("http://pythonscraping.com/pages/processing2.php", files=files)
print(r.text)