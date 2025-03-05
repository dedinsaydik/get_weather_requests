import requests


cities = ["Лондон", "svo", "Череповце"]


for city in cities:
    url = f"https://wttr.in/{city}"
    payload = {'n': '',
               'T': '',
               'q': '',
               'u': '',
               'lang': 'ru',
               '?M': '',
               '?m': '',
               '?n': '',
               '?q': ''}
    response = requests.get(url, params=payload)

    response.raise_for_status()
    print(response.text)
