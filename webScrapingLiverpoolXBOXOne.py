from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products=[] #List to store name of the product
prices=[] #List to store price of the product
#ratings=[] #List to store rating of the product
driver.get("https://www.liverpool.com.mx/tienda?s=xbox+one")
content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")
for a in soup.findAll('li', attrs={'class':'m-product__card card-masonry'}): 
    name=a.find('h5', attrs={'class':'card-title a-card-description'})
    price=a.find('p', attrs={'class':'a-card-discount'})
    #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    #ratings.append(rating.text)
    
print (products)
print (prices)

df = pd.DataFrame({'ProductName':products,'Price':prices,})
df.to_csv('liverpool Nintendo Switch.csv', index=False, encoding='utf-8')
