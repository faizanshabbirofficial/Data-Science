import requests
from bs4 import BeautifulSoup as Soup
import re

url = 'https://priceoye.pk/mobiles'
response = requests.get(url)
content = response.content

soup = Soup(content, 'html5lib')

products = soup.findAll('div', {'class': 'detail-box'})

scrapped = []
for product in products:
    name = product.find('h4', {'class': 'p3'}).text.strip()
    discounted_price = product.find('div', {'class': 'price-box'}).text.strip()
    price = product.find('div', {'class': 'price-diff-retail'})
    clean = re.compile('<.*?>')
    price = re.sub(clean, '', str(price))
    discount = product.find('div', {'class': 'price-diff-saving'})
    discount = re.sub(clean, '', str(discount))
    jsonObj = {"name": name, "discounted_price": discounted_price,
               "price": price.strip(), "discount": discount.strip()}
    scrapped.append(jsonObj)

for scrap in scrapped:
    print(scrap)
