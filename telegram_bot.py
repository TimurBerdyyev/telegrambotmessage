from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
bot_token = os.environ['TELEGRAM_BOT_API']

channel_id = '@nasa_epic_space'


bot = Bot(token=bot_token)


photo_path = 'images/epic_1b_20240308073922.png'


bot.send_photo(chat_id=channel_id, photo=open(photo_path, 'rb'))

