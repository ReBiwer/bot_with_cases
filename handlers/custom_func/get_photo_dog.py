import json, requests


def get_photo_dog():
    req_url_photo = requests.get('https://dog.ceo/api/breeds/image/random')
    data_req_url_photo = json.loads(req_url_photo.text)
    url_photo = data_req_url_photo['message']
    req_photo = requests.get(url_photo).content
    return req_photo
