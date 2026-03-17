import time
import board
import adafruit_dht

sensor = adafruit_dht.DHT11(board.D4)

print("Reading DHT Sensor on Pi 5 (GPIO 4)...")

while True:
    try:
        temperature_c = sensor.temperature
        humidity = sensor.humidity

        if humidity is not None and temperature_c is not None:
            print(f"Temp: {temperature_c:.1f} °C Humidity: {humidity}%")
        else:
            print("Sensor reading empty, retrying...")

    except RuntimeError as error:
        time.sleep(2.0)
        continue

    except Exception as error:
        sensor.exit()
        raise error

    except KeyboardInterrupt:
        print("\nExiting...")
        sensor.exit()
        break

    time.sleep(2.0)
