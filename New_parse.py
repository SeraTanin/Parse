import requests
from bs4 import BeautifulSoup as Bp
import sys
import os


url_link = 'http://www.guitar.by/forum/viewforum.php?f=43&sid=fc9677e454c4e6480f0109ca67c061b8'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
           'accept': '*/*'}
pages = ['&start=50', '&start=100', '&start=150', '&start=200']
HOST = 'http://www.guitar.by/forum'
FILE = 'pedals.csv'


urls = [url_link]
for page in pages:
    urls.append(url_link + page)
# print(urls)

def page_num():
    for num_count in range(1, 6):

        print(num_count)


for url in urls:
    page_num()
    r = requests.get(url, headers=headers)
    soup = Bp(r.text, features='html.parser')

    items = soup.find_all('a', class_="topictitle")

    pedals = []
    for item in items:
        pedals.append({
            'title': item.get_text(strip=True),
            'link': HOST + item.get('href').lstrip('.')
        })
    for i in pedals:
        boss_pedals = []
        i = str(i)
        low_reg = i.lower()

        if 'boss' in low_reg:
            boss_pedals.append(low_reg)
            print(boss_pedals)