# --＜注意＞----------------------------------
# pip install geocoderでインストールが必要
# -------------------------------------------
import geocoder

def get_coordinates(address):
    # OpenStreetMapを利用
    g = geocoder.osm(address)
    if g.ok:
        return g.lat, g.lng
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
