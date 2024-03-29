import requests

def download_and_save(url, filename):
    with open(filename, 'wb') as f:
        f.write(requests.get(url).content)
