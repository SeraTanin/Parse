import requests
from bs4 import BeautifulSoup
import csv
import os

url = 'http://www.guitar.by/forum/viewforum.php?f=43&sid=fc9677e454c4e6480f0109ca67c061b8'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
           'accept': '*/*'}
pages = ['&start=50', '&start=100', '&start=150', '&start=200']
HOST = 'http://www.guitar.by/forum'
FILE = 'pedals.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'lxml')
    pagination = soup.find_all('a', class_='button')

    return pagination

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('a', class_="topictitle")
    # name = input('Enter a name: ')
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


def search_name():
    pass


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['link']])


def parse():
    html = get_html(url)
    if html.status_code == 200:
        # pages_count = get_pages_count(html.text)
        pedals = get_content(html.text)
        pages = get_pages_count(html.text)
        # pedals = []
        # for page in pages:
        #     print(f'Парсинг страницы {page} из {pages_count}...')
        #     html = get_html(url, params={'page': page})
        #     pedals.extend(get_content(html.text))
        # save_file(pedals, FILE)
        # print(f'Получено {len(pedals)} автомобилей')
        # os.startfile(FILE)
    else:
        print('Error')


parse()
