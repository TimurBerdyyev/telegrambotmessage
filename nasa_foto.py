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

    for image_index, image_info in enumerate(content):
        image_url = image_info['url']
        extension = os.path.splitext(os.path.basename(image_url))[-1]
        image_response = requests.get(image_url)
        filename = f'nasa_images/nasa_image{image_index + 1}{extension}'
        download_and_save(image_url, filename)
        image_response.raise_for_status()

        with open(f'nasa_images/nasa_image{image_index + 1}{extension}', 'wb') as f:
            f.write(image_response.content)

        logger.info(f"Изображение {image_index + 1} успешно сохранено в nasa_images/nasa_image{image_index + 1}{extension}")


def main():
    logging.basicConfig(level=logging.ERROR)
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    fetch_nasa_images(api_key, count=3)


if __name__ == '__main__':
    main()
