from bs4 import BeautifulSoup
import requests


html = requests.get('http://www.python.org')
#print(html.text)

soup = BeautifulSoup(html.text, "html.parser")

titles = soup.find_all('title')
print(titles[0].text)

intro = soup.find_all('div', {'class': 'introduction'})
print(intro)
print(intro[0].text)