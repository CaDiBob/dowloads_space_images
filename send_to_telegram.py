import argparse
import os
import telegram
from dotenv import load_dotenv
from os import listdir
from os.path import isfile
from os.path import join
import time


def send_to_telegram(token, chat_id, sleep):
    folder = 'images/'
    bot = telegram.Bot(token=token)
    while True:
        for image in get_pictures(folder):
            image_path = f'{folder}{image}'
            with open(image_path, 'rb') as file:
                bot.send_photo(chat_id=chat_id, photo=file)
            time.sleep(sleep)


def get_pictures(folder):
    images = []
    for image in listdir(folder):
        if isfile(join(folder, image)):
            images.append(image)
        else:
            for file in listdir(join(folder, image)):
                images.append(f'{image}/{file}')
    return images


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'interval', help='Интервал публикации фото на канал в секундах'
        )
    namespace = parser.parse_args()
    sleep = int(namespace.interval)
    token = os.getenv('TG_API')
    chat_id = os.getenv('TG_CHAT_ID')
    send_to_telegram(token, chat_id, sleep)
