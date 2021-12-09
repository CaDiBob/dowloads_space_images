import os
import datetime
import requests
from dotenv import load_dotenv
from os.path import splitext
from urllib.parse import urlsplit
from urllib.parse import unquote
from download_image import download_image


def fetch_nasa_apod(token, nasa_apod_dir):
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': token,
        'start_date': '2020-10-01',
        'end_date': '2020-11-01',
    }
    response = requests.get(nasa_apod_url, params=params)
    response.raise_for_status()
    links = response.json()
    for apod_number, apod in enumerate(links):
        url = apod['url']
        ext = get_extension(url)
        filename = f'nasa_apod{apod_number}{ext}'
        filepath = f'{nasa_apod_dir}/{filename}'
        download_image(url, filepath, params)


def fetch_nasa_epic(token, nasa_epic_dir):
    nasa_epic_url = 'https://epic.gsfc.nasa.gov/api/natural'
    params = {'api_key': token}
    response = requests.get(nasa_epic_url, params=params)
    response.raise_for_status()
    for epic_number, epic in enumerate(response.json()):
        filename = f'nasa_epic{epic_number}.png'
        img_name = epic['image']
        img_date = datetime.datetime.fromisoformat(epic['date'])
        epic_date = img_date.strftime('%Y/%m/%d')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{img_name}.png'
        filepath = f'{nasa_epic_dir}/{filename}'
        download_image(url, filepath, params)


def get_extension(url):
    split_url = urlsplit(url).path
    split_filename = splitext(split_url)
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
