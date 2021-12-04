import os
import datetime
import requests
from dotenv import load_dotenv
from os.path import split
from os.path import splitext
from urllib.parse import urlsplit
from urllib.parse import unquote


def save_images(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_nasa_apod(token, nasa_apod_dir):
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': token,
        'start_date': '2020-10-01',
        'end_date': '2020-11-01',
    }
    response = requests.get(url_nasa, params=params)
    response.raise_for_status()
    response_dict = response.json()
    for apod_number, apod in enumerate(response_dict):
        url = apod['url']
        ext = get_extension(url)
        file = f'nasa_apod{apod_number}{ext}.jpg'
        path = f'{nasa_apod_dir}/{file}'
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


def get_extension(url):
    split_url = urlsplit(url)
    file_path = unquote(split_url[2])
    split_filename = splitext(file_path)
    extension = split_filename[1]
    return extension


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('API_NASA')
    nasa_apod_dir = 'images/nasa_apod'
    nasa_epic_dir = 'images/nasa_epic'
    os.makedirs(nasa_apod_dir, exist_ok=True)
    os.makedirs(nasa_epic_dir, exist_ok=True)
    fetch_nasa_epic(token, nasa_epic_dir)
    fetch_nasa_apod(token, nasa_apod_dir)