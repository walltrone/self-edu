import requests

BASE_URL = 'https://akabab.github.io/superhero-api/api'
SUPERHERO_NAMES = ['Hulk', 'Captain America', 'Thanos']
ALL_SUPERHERO = '/all.json'


def _get_superhero_list():
    response = requests.get(BASE_URL + ALL_SUPERHERO)
    return response.json()


def _get_superhero_intelligence(SUPERHERO_NAMES):
    superhero_list = _get_superhero_list()
    superhero_intelligence = {}
    for superhero in superhero_list:
        if superhero['name'] in SUPERHERO_NAMES:
            superhero_intelligence[superhero['powerstats']['intelligence']] = superhero['name']
    return superhero_intelligence


def who_is_smartest():
    superhero_intelligence = _get_superhero_intelligence(SUPERHERO_NAMES)
    intelligence = sorted(superhero_intelligence)
    return superhero_intelligence[intelligence[-1]]


print(f'Самый умный супергерой - {who_is_smartest()}')
