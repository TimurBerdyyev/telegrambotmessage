import requests

def download_and_save(url, image_path):
    with open(image_path, 'wb') as f:
        f.write(requests.get(url).content)
