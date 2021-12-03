import os
import telegram
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TG_API')
chat_id = '@CaD_space_images'
bot = telegram.Bot(token=token)
bot.send_message(chat_id=chat_id, text="Hi my friends it`s my first message!")
