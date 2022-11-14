import requests
from pprint import pprint
from bs4 import BeautifulSoup


URL = 'https://select.by/kurs'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0', 'accept': '*/*'}
r = requests.get(URL, headers=headers)
print(r.status_code)
soup = BeautifulSoup(r.text, 'lxml')
items = soup.find_all('tr', class_="text-center h4")
# pprint(items)
# item.find('svg', class_='svg_i16_pin').find_next('span').get_text() # Example
kursy = []
for item in items:
    kursy.append({
        'Kurs': item.find('span').get_text()

    })
print(kursy)

# print(soup.get_text())