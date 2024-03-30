import os
import time
from telegram import Bot
from dotenv import load_dotenv

def publish_photos(bot, photos_directory, telegram_channel_id):
    photos = os.listdir(photos_directory)
    if not photos:
        return

    for photo_name in photos:
        photo_path = os.path.join(photos_directory, photo_name)
        with open(photo_path, 'rb') as photo_file:
            bot.send_photo(chat_id=telegram_channel_id, photo=photo_file)
        time.sleep(10)

if __name__ == "__main__":
    load_dotenv()
    
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_API')
    TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
    PHOTOS_DIRECTORY = 'images'
    PUBLICATION_DELAY = int(os.getenv('PUBLICATION_DELAY', 4 * 60 * 60))

    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    publish_photos(bot, PHOTOS_DIRECTORY, TELEGRAM_CHANNEL_ID)
