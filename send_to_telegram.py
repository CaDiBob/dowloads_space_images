import argparse
import os
import telegram
import time
from dotenv import load_dotenv
from os import listdir
from os.path import isfile
from os.path import join


def send_to_telegram(token, chat_id, sleep):
    folder = 'images/'
    bot = telegram.Bot(token=token)
    while True:
        for image_name in get_image_names(folder):
            image_path = f'{folder}{image_name}'
            with open(image_path, 'rb') as file:
                bot.send_photo(chat_id=chat_id, photo=file)
            time.sleep(sleep)


def get_image_names(folder):
    images = []
    for image_folder in listdir(folder):
        if isfile(join(folder, image_folder)):
            images.append(image_folder)
        else:
            for filename in listdir(join(folder, image_folder)):
                images.append(f'{image_folder}/{filename}')
    return images


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'interval',
        help='Интервал публикации фото на канал в секундах',
        )
    namespace = parser.parse_args()
    sleep = int(namespace.interval)
    token = os.getenv('TG_API')
    chat_id = os.getenv('TG_CHAT_ID')
    send_to_telegram(token, chat_id, sleep)
