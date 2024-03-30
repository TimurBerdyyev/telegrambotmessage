import requests

def download_and_save(url, image_path):
    response = requests.get(url)
    
    try:
        response.raise_for_status()
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print("Файл успешно загружен и сохранен.")
    except requests.exceptions.HTTPError as error:
        print(f"Ошибка загрузки файла: {error}")
