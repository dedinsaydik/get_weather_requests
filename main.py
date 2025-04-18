import requests
from urllib.parse import urljoin


cities = ["Лондон", "svo", "Череповец"]


for city in cities:
    url = urljoin("https://wttr.in/", city)
    payload = {'n': '',
               'T': '',
               'q': '',
               'lang': 'ru',
               'M': ''}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)