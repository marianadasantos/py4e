import requests
from bs4 import BeautifulSoup

response = requests.get('https://gl.globo.com/')
#shows content
content = response.content
#converts to object; ('content')= variable; (html)= format of the content, (.parse)= tells it to convert it to html  
site = BeautifulSoup('content', 'html.parse')
#('div')= name; (attrs)= attribute; ({:})= dictioinary: ({'class':'blabla'})
news = site.find('div', attrs={'class':'feed-post-body'})
title = news.find('a', attrs={'class':'feed-post-link'})
subtitle = title.find('div', attrs={'class':'feed-post-body-resumo'})

#prettify= shows it in an organized format
print(news.prettify())
#.text= showsn only the text, not all the code with tags etc
print(title.text)
print(subtitle.text)