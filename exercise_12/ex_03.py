import re 
import ssl
import urllib.parse, urllib.request, urllib.error

count = dict()
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urllib.request.urlopen(url).read()
for p in html:
    links = re.findall(b'<p>.+?</p>', html)
    print(links)
