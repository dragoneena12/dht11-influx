import RPi.GPIO as GPIO
import dht11
import time
import datetime
from influxdb import InfluxDBClient
from socket import gethostname

# Initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(pin=24)

# Database Connection
client = InfluxDBClient(host="influxDB", port=8086, database="dht11")
client.create_database("dht11")

try:
    while True:
        result = instance.read()
        if result.is_valid():
            json_body = [
                {
                    "measurement": "dht11",
                    "tags": {"host": gethostname()},
                    "time": str(datetime.datetime.now()),
                    "fields": {
                        "temperature": result.temperature,
                        "humidity": result.humidity,
                    },
                }
            ]
            client.write_points(json_body)
        time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
    client.close()
