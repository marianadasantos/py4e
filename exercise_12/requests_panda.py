import requests
from bs4 import BeautifulSoup
import pandas as pd

news_list= []

response = requests.get('https://www.g1.golobo.com/')
content = response.text
site = BeautifulSoup(content, 'html.parser')
news = site.findAll('div', attrs={'class':'feed-post-body'})

for each_news in news:
    title = news.find('a', attrs={'class':'feed-post-link'})
    subtitle = news.title.find('div', attrs={'class':'feed-post-body-resumo'})
    if (subtitle):
        news_list.append([title.text, subtitle.text, title['href']])
    else:
        news_list.append([title.text, '', title['href']])

news = pd.DataFrame(news_list, columns=['Title', 'Subtitle', 'Link'])
print(news)

