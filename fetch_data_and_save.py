import requests


def fetch_data_and_save(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    
    with open(filename, 'wb') as f:
        f.write(response.content)

    return response


