import requests
from requests.exceptions import HTTPError


CITIES = ['Лондон', 'Череповец', 'Шереметьево']
PAYLOAD = {'lang': 'ru', 'nTqm': ''}


def print_weather(site_url):
    response = requests.get(site_url, params=PAYLOAD)
    try:
        response.raise_for_status()
        print(response.text)
    except HTTPError:
        print('Прогноз недоступен')


if __name__ == '__main__':
    for city in CITIES:
        url = f'http://wttr.dvmn.org/{city}'
        print_weather(url)
