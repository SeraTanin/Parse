import requests
from bs4 import BeautifulSoup as Bp
from datetime import time
import csv
import sys
import os


url_link = 'http://www.guitar.by/forum/viewforum.php?f=43&sid=fc9677e454c4e6480f0109ca67c061b8'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
           'accept': '*/*'}
pages = ['&start=50', '&start=100', '&start=150', '&start=200']
HOST = 'http://www.guitar.by/forum'
FILE = 'pedals.csv'



def get_pages():
    for page in pages:
        urls.append(url_link + page)
    return urls


def get_list_of_pedals():
    page_list = 1
    for url in urls:


        print(f"Parsing page # {page_list}...\n")
        r = requests.get(url, headers=headers)
        soup = Bp(r.text, features='html.parser')
        items = soup.find_all('a', class_="topictitle")

        for item in items:
            if 'boss' in item.get_text(strip=True).lower():
                pedals.append({
                    'title': item.get_text(strip=True),
                    'link': HOST + item.get('href').lstrip('.')
                })

                print(f"{item.get_text(strip=True), HOST + item.get('href').lstrip('.')}\n")
        page_list += 1


def write_to_csv_file(items, path):
    with open(path, 'a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(['Название', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['link']])


if __name__ == '__main__':
    pedals = []
    urls = [url_link]
    get_pages()
    get_list_of_pedals()
    write_to_csv_file('items', 'boss_pedals.csv')
