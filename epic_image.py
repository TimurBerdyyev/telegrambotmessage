import os
import requests

from dotenv import load_dotenv

def get_epic_images(api_key, count=5):
    try:
        url_info = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}'
        response = requests.get(url_info)
        response.raise_for_status()

        data = response.json()
        if data:
            os.makedirs('earth_images', exist_ok=True)
            for image_info in data[:count]:
                image_date = image_info['date'][:10].replace('-', '/')
                image_name = image_info['image']
                image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?api_key={api_key}"

                # Скачиваем изображение
                response = requests.get(image_url)
                response.raise_for_status()

                # Сохраняем изображение
                with open(f'earth_images/{image_name}.png', 'wb') as f:
                    f.write(response.content)
                    print(f"Изображение {image_name}.png успешно сохранено")

        else:
            print("Информация об изображениях отсутствует.")

    except requests.exceptions.RequestException as e:
        print(f'Ошибка запроса: {e}')
    except Exception as e:
        print(f'Произошла ошибка: {e}')


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    get_epic_images(api_key, count=5)