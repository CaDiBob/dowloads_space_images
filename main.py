import os
import datetime
import requests
from dotenv import load_dotenv


def save_images(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(spacex_dir):
    url_spacex = 'https://api.spacexdata.com/v4/launches/618faad2563d69573ed8ca9d'
    params = None
    response = requests.get(url_spacex, params=params)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for link_number, url in enumerate(links):
        file = f'spacex{link_number}.jpg'
        path = f'{spacex_dir}/{file}'
        save_images(url, path, params)


def fetch_nasa_apod(token, nasa_apod_dir):
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': token,
        'start_date': '2021-10-30',
        'end_date': '2021-12-01',
    }
    response = requests.get(url_nasa, params=params)
    response.raise_for_status()
    response_dict = response.json()
    for item_number, item in enumerate(response_dict):
        file = f'nasa_apod{item_number}.jpg'
        path = f'{nasa_apod_dir}/{file}'
        url = item['url']
        save_images(url, path, params)


def fetch_nasa_epic(token, nasa_epic_dir):
    url_nasa_epic = 'https://epic.gsfc.nasa.gov/api/natural'
    params = {'api_key': token}
    response = requests.get(url_nasa_epic, params=params)
    response.raise_for_status()
    for epic_number, epic in enumerate(response.json()):
        file = f'nasa_epic{epic_number}.png'
        img_name = epic['image']
        img_date = datetime.datetime.fromisoformat(epic['date'])
        epic_date = img_date.strftime('%Y/%m/%d')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{img_name}.png'
        path = f'{nasa_epic_dir}/{file}'
        save_images(url, path, params)


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('API_NASA')
    spacex_dir = 'spacex'
    nasa_apod_dir = 'nasa_apod'
    nasa_epic_dir = 'nasa_epic'
    os.makedirs(nasa_apod_dir, exist_ok=True)
    os.makedirs(nasa_epic_dir, exist_ok=True)
    os.makedirs(spacex_dir, exist_ok=True)
    fetch_nasa_epic(token, nasa_epic_dir)
    fetch_nasa_apod(token, nasa_apod_dir)
    fetch_spacex_last_launch(spacex_dir)
