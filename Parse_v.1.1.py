import requests
from bs4 import BeautifulSoup


url_parse = 'https://www.guitar.by/forum/viewforum.php?f=43&sid=cb129b26afa35796f42d1829f68c720d'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
           'accept': '*/*'}
HOST = 'http://www.guitar.by/forum'


def get_html(url=url_parse):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features='html.parser')
    items = soup.find_all('a', class_="topictitle")
    pedals = []
    for item in items:
        get_text = item.get_text(strip=True)
    # return get_text
        if 'boss' in get_text.lower():
            pedals.append({
                'title': item.get_text(strip=True),
                'link': HOST + item.get('href').lstrip('.')
            })
    return pedals


def get_pages():
    while True:
        urls = [url_parse]
        for url in urls:
            r = requests.get(url=url_parse)
            soup = BeautifulSoup(r.text, features='html.parser')
            num_active_page = soup.find('li', class_='active').find_next().get_text()
            active_page = soup.find('li', class_='active').find_next()

            link_to_next_page = HOST + active_page.find_next('a', class_='button').get('href')[1:]
            urls.append(link_to_next_page)
            # full_link_to_next_page = HOST + link_to_next_page[1:]
            # next_page = HOST + link_to_next_page
            if len(urls) > 5:
                break
        return urls


def change_pages():
    pass

if __name__ == '__main__':
    print(get_pages())