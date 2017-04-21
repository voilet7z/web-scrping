import socks
import socket
from urllib.request import urlopen

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket
print(urlopen("https://www.google.com").read())