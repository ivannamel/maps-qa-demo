import requests
from config import BASE_URL

def test_reverse_geocode_eiffel():
    params = {"lat":48.858370, "lon":2.294481, "format":"json"}
    resp = requests.get(
        f"{BASE_URL}/reverse",
        params = {"lat": 48.85837, "lon": 2.294481, "format": "json"},
        headers = HEADERS
    )
    assert resp.status_code == 200
    address = resp.json().get("address", {})
    city = address.get("city") or address.get("town") or ""
    assert "Paris" in city
