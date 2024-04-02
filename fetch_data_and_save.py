import requests

def download_and_save(url, image_path):
    response = requests.get(url)
    
    response.raise_for_status()
    with open(image_path, 'wb') as f:
        f.write(response.content)
    print("Файл успешно загружен и сохранен.")
    
