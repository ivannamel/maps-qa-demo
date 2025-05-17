import math, requests
from config import BASE_URL, HEADERS
def distance(lat1, lon1, lat2, lon2):
    return math.hypot(lat1-lat2, lon1-lon2)

def test_geocode_empire_state():
    resp = requests.get(
        f"{BASE_URL}/search",
        params = {"q": "Empire State Building", "format": "json"},
        headers = HEADERS
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data, "Ожидали хотя бы один результат"
    lat, lon = float(data[0]["lat"]), float(data[0]["lon"])
    exp_lat, exp_lon = 40.748817, -73.985428
    assert distance(lat, lon, exp_lat, exp_lon) < 0.01

