import requests

api_static = "http://static-maps.yandex.ru/1.x/"
api_geocode = "http://geocode-maps.yandex.ru/1.x/"


def geocode(address):
    params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"
    }
    response = requests.get(api_geocode, params)
    if response:
        json_response = response.json()
        toponym_coordinates = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]["Point"]["pos"]
        return toponym_coordinates


def image_map(delta, address=None, lon=None, lat=None, up=0, r=0):
    if address:
        toponym_coordinates = geocode(address)
        lon, lat = toponym_coordinates.split(" ")

    # delta = "0.002"
    params = {
        "ll": ",".join([str(float(lon) + r), str(float(lat) + up)]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    response = requests.get(api_static, params=params)
    if response:
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)

    return lon, lat, delta

