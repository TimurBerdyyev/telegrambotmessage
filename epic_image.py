import os
import requests
from dotenv import load_dotenv
from logger_config import getLogger


logger = getLogger()

def get_epic_images(api_key, count=5):
    try:
        url_natural_images = 'https://api.nasa.gov/EPIC/api/natural/images'
        params = {'api_key': api_key}
        response = requests.get(url_natural_images, params=params)
        response.raise_for_status()
        json_content = response.json()

        if not json_content:
            logger.info("Информация об изображениях отсутствует.")
            return

        os.makedirs('images', exist_ok=True)
        for image_info in json_content[:count]:
            image_date = image_info['date'][:10].replace('-', '/')
            image_name = image_info['image']
            image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png"
            response = requests.get(image_url, params=params)
            response.raise_for_status()
            with open(f'images/{image_name}.png', 'wb') as f:
                f.write(response.content)
            logger.info(f"Изображение {image_name}.png успешно сохранено")

    except requests.RequestException as e:
        logger.error(f"Ошибка при запросе: {e}")

if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    get_epic_images(api_key, count=5)
