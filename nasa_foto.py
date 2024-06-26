import os
import requests
from dotenv import load_dotenv
import logging

from fetch_data_and_save import download_and_save

logger = logging.getLogger(__file__)


def fetch_nasa_images(api_key, count=5):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_key, 'count': count}
    response = requests.get(url, params=params)
    response.raise_for_status()

    content = response.json()
    os.makedirs('nasa_images', exist_ok=True)

    for index_image, image in enumerate(content, start=1):
        image_url = image['url']
        extension = os.path.splitext(os.path.basename(image_url))[-1]
    
        image_path = f'nasa_images/nasa_image{index_image}{extension}'
        download_and_save(image_url, image_path)
        


        logger.info(f"Изображение {index_image} успешно сохранено в {image_path}")


def main():
    logging.basicConfig(level=logging.ERROR)
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    fetch_nasa_images(api_key, count=3)


if __name__ == '__main__':
    main()
