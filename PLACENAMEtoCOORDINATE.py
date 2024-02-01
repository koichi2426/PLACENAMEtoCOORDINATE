# --＜注意＞----------------------------------
# pip install requestsでインストールが必要
# -------------------------------------------
import requests

def get_coordinates(address):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': address,
        'format': 'json'
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        results = response.json()
        if results:
            # 最初の結果の緯度と経度を取得
            latitude = results[0]['lat']
            longitude = results[0]['lon']
            return latitude, longitude
        else:
            print("No results found for the given address.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

# 使用例
address = "エッフェル塔"
coordinates = get_coordinates(address)

if coordinates:
    print(f"Address: {address}\nCoordinates: {coordinates}")
else:
    print("Coordinates could not be retrieved.")
