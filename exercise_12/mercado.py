import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
table = list()

url = 'https://lista.mercadolivre.com.br/'
product_name = input('Enter a product: ')

response = requests.get(url + product_name)

site = BeautifulSoup(response.text, 'html.parser')

products = site.findAll('div', attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for product in products:
    name = product.find('h2', attrs={'class':'ui-search-item__title'})
    link = product.find('a', attrs={'class':'ui-search-link'})
    price_code = product.find('span', attrs={'class':'price-tag ui-search-price__part'})
    real = price_code.find('span', attrs={'class':'price-tag-fraction'})
    cents = price_code.find('span', attrs={'class':'price-tag-cents'})

    print('Title:', name.text)
    print('Link:', link['href'])
    
#colocar função/variavel dentro de uma 'string': {} = valor fica ali dentro, .format(as variáveis/funções)
    if cents:
        juju = 'Price: R${},{}'.format(real.text, cents.text)
    else:
        juju = 'Price: R${},00'.format(real.text)
    
    print(juju)
    print('\n\n')
    table.append([name.text, juju, link['href']])

products = pd.DataFrame(table, columns=['Produto', 'Preço', 'Link'])
print(products)

