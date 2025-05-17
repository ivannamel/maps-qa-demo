# mock_server.py

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/search")
def search():
    q = request.args.get("q", "").lower()
    # Заготовки для тестов
    if "statue of liberty" in q:
        return jsonify([{"lat": "40.689249", "lon": "-74.044500"}])
    if "empire state building" in q:
        return jsonify([{"lat": "40.748817", "lon": "-73.985428"}])
    # дефолтный пустой результат
    return jsonify([]), 200

@app.route("/reverse")
def reverse():
    lat = float(request.args.get("lat", 0))
    lon = float(request.args.get("lon", 0))
    # Эйфелева башня
    if abs(lat - 48.858370) < 0.001 and abs(lon - 2.294481) < 0.001:
        return jsonify({"address": {"city": "Paris"}})
    return jsonify({"address": {}}), 200

if __name__ == "__main__":
    # Запускаем на порту 8080
    app.run(host="0.0.0.0", port=8080)

