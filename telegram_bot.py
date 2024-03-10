from telegram import Bot
from dotenv import load_dotenv
import os


load_dotenv()

bot = Bot(token=os.environ['TELEGRAM_BOT_API'])


channel_id = '@nasa_epic_space'


bot.send_message(chat_id=channel_id, text='Привет, это тестовое сообщение от бота!')
