# --＜注意＞----------------------------------
# pip install geopyでインストールが必要
# -------------------------------------------
from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        print("No results found for the given address.")
        return None

# 使用例
address = "エッフェル塔"
coordinates = get_coordinates(address)

if coordinates:
    print(f"Address: {address}\nCoordinates: {coordinates}")
else:
    print("Coordinates could not be retrieved.")
