import requests

api_server = "http://static-maps.yandex.ru/1.x/"
api_server1 = "http://geocode-maps.yandex.ru/1.x/"


def image_map(adress=None, lon=None, lat=None):
    if not adress:
        delta = "0.002"
        params = {
            "ll": ",".join([lon, lat]),
            "spn": ",".join([delta, delta]),
            "l": "map"
        }
        response = requests.get(api_server, params=params)
        if response:
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
    else:
        params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": 'Москва, ул. Ак. Королева, 12',
            "format": "json"
        }
        response = requests.get(api_server1, params)
        if response:
            json_response = response.json()
            toponym_coodrinates = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]["Point"]["pos"]
            toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
            delta = "0.005"
            map_params = {
                "ll": ",".join([toponym_longitude, toponym_lattitude]),
                "spn": ",".join([delta, delta]),
                "l": "map"
            }
            response = requests.get(api_server, map_params)
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)

