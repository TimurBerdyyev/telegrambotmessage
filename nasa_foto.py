import os
from dotenv import load_dotenv
import requests
import logging

def fetch_nasa_images(api_key, count=5):
    try:
        url = 'https://api.nasa.gov/planetary/apod'
        params = {'api_key': api_key, 'count': count}

        response = requests.get(url, params=params)
        response.raise_for_status()

        if response.status_code != 200:
            logging.error(f"Ошибка при получении данных: {response.status_code}")
            return

        apod_data = response.json()
        os.makedirs('images', exist_ok=True)
        for idx, image_data in enumerate(apod_data):
            image_url = image_data['url']
            extension = os.path.splitext(os.path.basename(image_url))[-1]
            with open(f'nasa_images/nasa_image{idx + 1}{extension}', 'wb') as f:
                image_response = requests.get(image_url)
                f.write(image_response.content)
                logging.info(f"Изображение {idx + 1} успешно сохранено в nasa_images/nasa_image{idx + 1}{extension}")

    except requests.RequestException as e:
        logging.error(f"Ошибка при запросе: {e}")

if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    logging.basicConfig(level=logging.INFO)
    fetch_nasa_images(api_key, count=3)
