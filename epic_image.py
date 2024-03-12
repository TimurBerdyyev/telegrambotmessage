import os
import requests
from dotenv import load_dotenv

import logging

logging.basicConfig(level=logging.INFO)

def get_epic_images(api_key, count=5):
    url_natural_images = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': api_key}
    response = requests.get(url_natural_images, params=params)
    response.raise_for_status()
    response_data = response.json()

    if response_data:
        os.makedirs('images', exist_ok=True)
        for image_info in response_data[:count]:
            image_date = image_info['date'][:10].replace('-', '/')
            image_name = image_info['image']
            image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png"
            response = requests.get(image_url, params=params)
            response.raise_for_status()
            with open(f'images/{image_name}.png', 'wb') as f:
                f.write(response.content)
            logging.info(f"Изображение {image_name}.png успешно сохранено")

    else:
        logging.info("Информация об изображениях отсутствует.")

if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    get_epic_images(api_key, count=5)
