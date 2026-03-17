from flask import Flask, render_template
import requests

app = Flask(__name__)

LAT = 18.491
LON = 74.018
LOCATION = "MIT ADT Campus"

URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=temperature_2m,relative_humidity_2m"

@app.route('/')
def home():
    temp = "--"
    humidity = "--"

    try:
        response = requests.get(URL)
        data = response.json()

        current = data.get('current', {})
        temp = current.get('temperature_2m', 'N/A')
        humidity = current.get('relative_humidity_2m', 'N/A')

    except Exception as e:
        print("Error:", e)

    return render_template('index.html', place=LOCATION, temp=temp, hum=humidity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
