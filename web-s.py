
#from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
#driver = webdriver.Chrome(r"E:\software files\Web drivers\chromedriver")
res = requests.get("https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_3&otracker1=AS_QueryStore_OrganicAutoSuggest_0_3&as-pos=0&as-type=RECENT&as-backfill=on")
products=[]#List to store name of the product
prices=[]#List to store price of the product
ratings=[] #List to store rating of the product
#driver.get("https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_3&otracker1=AS_QueryStore_OrganicAutoSuggest_0_3&as-pos=0&as-type=RECENT&as-backfill=on")
#print(res)
#content = driver.page_source
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())

for a in soup.find_all('a', href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
