import os
import requests as r



# def spacex_image(url, folder_page):
#     response = r.get(url)
#     os.makedirs(folder_page, exist_ok=True)
#     with open(os.path.join(folder_page, 'hubble.jpeg'), 'wb') as f:
#         f.write(response.content)
#     print('изображение успешно загруженно!')
#
# url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
# folder_page = 'spacex_photo'
#
# spacex_image(url, folder_page)

# def get_launch_info(launch_id):
#     url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
#     try:
#         response = r.get(url)
#         response.raise_for_status()
#         return response.json()
#     except r.exceptions.HTTPError as err:
#         print(f"Ошибка при получении данных о запуске: {err}")
#         return None

# def download_images_from_launch(launch_info):
#     if launch_info:
#         print("Ссылки на фотографии с запуска SpaceX:")
#         flickr_links = launch_info.get('links', {}).get('flickr', {}).get('original', [])
#         for idx, image_url in enumerate(flickr_links):
#             image_data = r.get(image_url)
#             image_name = f'spacex_{idx + 1}.jpg'
#             image_path = os.path.join('images', image_name)
#             with open(image_path, 'wb') as image_file:
#                 image_file.write(image_data.content)
#                 print(f"Скачано изображение {image_name}")
#         print(f"Скачивание изображений с запуска SpaceX завершено. Все изображения сохранены в папке images.")
#     else:
#         print("Не удалось получить информацию о запуске.")
#
# # Пример использования обеих функций
# launch_id = "5eb87d47ffd86e000604b38a"  # Пример ID запуска
# launch_info = get_launch_info(launch_id)
# download_images_from_launch(launch_info)



def fetch_spacex_launch_photos(launch_id):
    try:
        url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
        response = r.get(url)
        response.raise_for_status()

        photos = response.json().get("links", {}).get("flickr", {}).get("original", [])

        if photos:
            print(f"Найдено {len(photos)} фотографий.")
            os.makedirs('images', exist_ok=True)
            for idx, photo_url in enumerate(photos):
                with open(f"images/spacex{idx + 1}.jpg", 'wb') as f:
                    photo_response = r.get(photo_url)
                    f.write(photo_response.content)
                    print(f" {idx + 1} скачано")
        else:
            print("Список фотографий пуст.")
    except r.RequestException as e:
        print(f"Ошибка при запросе: {str(e)}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    launch_id = "5eb87d47ffd86e000604b38a"
    fetch_spacex_launch_photos(launch_id)


