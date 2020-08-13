import requests
from requests.exceptions import HTTPError


cities = ['Лондон', 'Череповец', 'Шереметьево']
payload = {"lang": "ru"}


def print_weather(site_url):
    response = requests.get(site_url, params=payload)
    try:
        response.raise_for_status()
        print(response.text)
    except HTTPError:
        print('Прогноз недоступен')


if __name__ == '__main__':
    for city in cities:
        url = f'http://wttr.dvmn.org/{city}?nTqm'
        print_weather(url)
