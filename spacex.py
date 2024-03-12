import os
import argparse
import requests as r
from logger_config import getLogger


logger = getLogger()

def fetch_spacex_launch_photos(launch_id):
    try:
        url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
        response = r.get(url)
        response.raise_for_status()

        decoded_response = response.json()
        if 'error' in decoded_response:
            raise r.exceptions.HTTPError(decoded_response['error'])

        photos = decoded_response.get("links", {}).get("flickr", {}).get("original", [])
        if not photos:
            logger.warning("Список фотографий пуст.")
            return

        logger.info(f"Найдено {len(photos)} фотографий.")
        os.makedirs('images', exist_ok=True)
        for idx, photo_url in enumerate(photos):
            with open(f"images/spacex{idx + 1}.jpg", 'wb') as f:
                photo_response = r.get(photo_url)
                f.write(photo_response.content)
                logger.info(f"Фото {idx + 1} скачано")

    except r.exceptions.HTTPError as e:
        logger.error(f"Ошибка HTTP: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch SpaceX launch photos')
    parser.add_argument('launch_id', type=str, help='ID of the SpaceX launch')
    args = parser.parse_args()

    fetch_spacex_launch_photos(args.launch_id)
