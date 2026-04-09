from flask import Flask, jsonify
import json

app = Flask(__name__)

with open("Assignment10/airports.json", "r", encoding="utf-8") as f:
    airports = json.load(f)

@app.route('/airport/<icao>')
def get_airport(icao):
    icao = icao.upper()

    if icao in airports:
        airport = airports[icao]
        return jsonify({
            "icao": airport["icao"],
            "name": airport["name"],
            "city": airport["city"],
            "country": airport["country"]
        })

    return jsonify({"error": "Airport not found"})

if __name__ == '__main__':
    app.run(debug=True)
