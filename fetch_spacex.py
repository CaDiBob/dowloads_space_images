import os
import requests
from dotenv import load_dotenv
from download_image import download_image


def fetch_spacex_last_launch(spacex_dir):
    spacex_url = 'https://api.spacexdata.com/v4/launches/618faad2563d69573ed8ca9d'
    response = requests.get(spacex_url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for link_number, url in enumerate(links):
        filename = f'spacex{link_number}.jpg'
        filepath = f'{spacex_dir}/{filename}'
        download_image(url, filepath)


if __name__ == '__main__':
    spacex_dir = 'images/spacex'
    os.makedirs(spacex_dir, exist_ok=True)
    fetch_spacex_last_launch(spacex_dir)
