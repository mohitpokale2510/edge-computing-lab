import requests
import random
import time

URL = "http://data-logger:8000/log"

while True:
    temp = round(random.uniform(20, 30), 2)
    
    try:
        response = requests.post(URL, json={"temperature": temp})
        print(f"Sent {temp}°C → Status {response.status_code}")
    except Exception as e:
        print("Error:", e)

    time.sleep(5)
