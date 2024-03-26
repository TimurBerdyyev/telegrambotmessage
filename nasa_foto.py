import os
import requests
from dotenv import load_dotenv
from logger_config import getLogger

logger = getLogger()

def fetch_nasa_images(api_key, count=5):
    try:
        url = 'https://api.nasa.gov/planetary/apod'
        params = {'api_key': api_key, 'count': count}

        response = requests.get(url, params=params)
        response.raise_for_status()

        if response.status_code != 200:
            logger.error(f"Ошибка при получении данных: {response.status_code}")
            return

        content = response.json()

        os.makedirs('nasa_images', exist_ok=True)

        for index, image_info in enumerate(content):
            image_url = image_info['url']
            extension = os.path.splitext(os.path.basename(image_url))[-1]

            with open(f'images/nasa_image{idx + 1}{extension}', 'wb') as f:
                image_response = requests.get(image_url)
                f.write(image_response.content)

            logger.info(f"Изображение {idex + 1} успешно сохранено в nasa_images/nasa_image{idex + 1}{extension}")

    except requests.RequestException as e:
        logger.error(f"Ошибка при запросе: {e}")

if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    fetch_nasa_images(api_key, count=3)
