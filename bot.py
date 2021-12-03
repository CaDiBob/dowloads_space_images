import os
import telegram
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TG_API')
chat_id = os.getenv('TG_CHAT_ID')
bot = telegram.Bot(token=token)
bot.send_document(chat_id=chat_id, document=open('nasa_epic/nasa_epic0.png', 'rb'))
