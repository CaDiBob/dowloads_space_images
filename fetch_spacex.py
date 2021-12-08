import os
import requests
from dotenv import load_dotenv
from fetch_nasa import save_images


def fetch_spacex_last_launch(spacex_dir):
    url_spacex = 'https://api.spacexdata.com/v4/launches/618faad2563d69573ed8ca9d'
    response = requests.get(url_spacex)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for link_number, url in enumerate(links):
        filename = f'spacex{link_number}.jpg'
        filepath = f'{spacex_dir}/{filename}'
        save_images(url, filepath)


if __name__ == '__main__':
    spacex_dir = 'images/spacex'
    os.makedirs(spacex_dir, exist_ok=True)
    fetch_spacex_last_launch(spacex_dir)