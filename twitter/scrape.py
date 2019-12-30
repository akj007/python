import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://pixabay.com/images/search/wallpaper/'

page = requests.get(url)
soup = bs(page.text, 'html.parser')
#print(soup)
images = soup.findAll('img')

if not os.path.exists('wallp'):
    os.makedirs('wallp')

os.chdir('wallp')

x = 0

for image in images:
    try:
        url = image['src']
        print(url)
        source = requests.get(url)
        if source.status_code == 200:
            with open('wallp-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x+=1
    except:
        print("xyz")
        pass
