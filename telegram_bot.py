import os
import random
import time
from telegram import Bot
from dotenv import load_dotenv
from requests.exceptions import HTTPError

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_API')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

PHOTOS_DIRECTORY = 'images'
PUBLICATION_DELAY = int(os.getenv('PUBLICATION_DELAY', 4 * 60 * 60))

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def publish_photos():
    try:
        photos = os.listdir(PHOTOS_DIRECTORY)
        if not photos:
            print("Нет фотографий для публикации.")
            return

        random.shuffle(photos)
        for photo_name in photos:
            photo_path = os.path.join(PHOTOS_DIRECTORY, photo_name)
            try:
                with open(photo_path, 'rb') as photo_file:
                    bot.send_photo(chat_id=TELEGRAM_CHANNEL_ID, photo=photo_file)
                    print(f"Отправлено: {photo_name}")
            except FileNotFoundError:
                print(f"Файл не найден: {photo_name}")
            except Exception as e:
                print(f"Ошибка при отправке {photo_name}: {e}")
            time.sleep(10)
    except OSError as e:
        print(f"Ошибка операционной системы: {e}")
    except HTTPError as e:
        print(f"Ошибка HTTP: {e}")

if __name__ == "__main__":
    while True:
        publish_photos()
        print(f"Публикация завершена. Ожидание {PUBLICATION_DELAY} секунд.")
        time.sleep(PUBLICATION_DELAY)
