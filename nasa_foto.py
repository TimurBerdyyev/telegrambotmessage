import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import requests


def fetch_nasa_image(api_key, count=5):
    try:
        url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&count={count}'
        response = requests.get(url)
        response.raise_for_status()

        apod_data = response.json()
        os.makedirs('images', exist_ok=True)
        for idx, image_data in enumerate(apod_data):
            image_url = image_data['url']
            extension = os.path.splitext(urlparse(image_url).path)[-1]
            with open(f'nasa_images/nasa_image{idx + 1}{extension}', 'wb') as f:
                f.write(requests.get(image_url).content)
                print(f"Изображение {idx + 1} успешно сохранено в nasa_images/nasa_image{idx + 1}{extension}")

    except requests.exceptions.HTTPError as e:
        print(f'HTTP ошибка: {e}')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    fetch_nasa_image(api_key, count=3)






