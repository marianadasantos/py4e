import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.w3schools.com/python/ref_dictionary_get.asp')

content = response.content
site = BeautifulSoup(content, 'html.parser')
escrito = site.find('div', attrs={'class':'w3-code w3-border notranslate'})
print(escrito)