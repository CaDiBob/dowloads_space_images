import os
import requests
from dotenv import load_dotenv
from fetch_nasa import save_images


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


if __name__ == '__main__':
    spacex_dir = 'images/spacex'
    os.makedirs(spacex_dir, exist_ok=True)
    fetch_spacex_last_launch(spacex_dir)