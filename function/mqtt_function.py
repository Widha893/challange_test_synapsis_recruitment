import random
import json
import os
from datetime import datetime
import csv

class MqttPublisher:

    def __init__(self, mqtt_client, mqtt_topic, kandidat_name):
        self.mqtt_client = mqtt_client
        self.mqtt_topic = mqtt_topic
        self.kandidat_name = kandidat_name

    def getTimestampUtc(self):
        now_utc = datetime.utcnow()
        return now_utc.strftime("%Y-%m-%d %H:%M:%S")

    def getTimestampGmt7(self):
        now_utc = datetime.utcnow()
        gmt7 = now_utc.timestamp() + (7 * 3600)
        local_time = datetime.fromtimestamp(gmt7)
        return local_time.strftime("%Y-%m-%d %H:%M:%S")

    def readWeatherData(self):
        try:
            log_folder = os.path.join(os.getcwd(), "log")
            json_path = os.path.join(log_folder, "data_weather.json")

            with open(json_path, "r") as f:
                data = json.load(f)

            temp = data.get("temperature", 0.0)
            humidity = data.get("humidity", 0.0)

            return float(temp), float(humidity)
        except Exception as e:
            print(f"ERROR reading data_weather.json: {e}")
            return 0.0, 0.0

    def generateSensorData(self):
        sensor1 = random.randint(0, 100)
        sensor2 = round(random.uniform(0, 1000), 2)
        sensor3 = random.choice([True, False])
        sensor4, sensor5 = self.readWeatherData()

        return sensor1, sensor2, sensor3, sensor4, sensor5

    def publishData(self):
        timestamp_utc = self.getTimestampUtc()
        timestamp_gmt7 = self.getTimestampGmt7()

        sensor1, sensor2, sensor3, sensor4, sensor5 = self.generateSensorData()

        payload = {
            "nama": self.kandidat_name,
            "data": {
                "sensor1": sensor1,
                "sensor2": sensor2,
                "sensor3": sensor3,
                "sensor4": sensor4,
                "sensor5": sensor5
            },
            "timestamp": timestamp_utc
        }

        try:
            result = self.mqtt_client.publish(self.mqtt_topic, json.dumps(payload))
            state = "Success" if result.rc == 0 else "Failed"
        except Exception as e:
            print(f"ERROR publishing MQTT: {e}")
            state = "Failed"

        # Print console log
        print(f"Timestamp : {timestamp_gmt7}")
        print(f"Action    : Publish")
        print(f"Topic     : {self.mqtt_topic}")
        print(f"Data      : {json.dumps(payload)}")
        print(f"State     : {state}")
        print("-" * 50)

        # Log to CSV
        self.logToCsv(timestamp_gmt7, sensor1, sensor2, sensor3, sensor4, sensor5, state)

    def logToCsv(self, timestamp, s1, s2, s3, s4, s5, state):
        log_folder = os.path.join(os.getcwd(), "log")
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        today = datetime.now()
        filename = f"mqtt_log_{today.strftime('%d%m%y')}.csv"
        csv_path = os.path.join(log_folder, filename)

        file_exists = os.path.isfile(csv_path)

        with open(csv_path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=';')

            if not file_exists:
                writer.writerow(["timestamp", "sensor1", "sensor2", "sensor3", "sensor4", "sensor5", "status"])

            writer.writerow([timestamp, s1, s2, s3, s4, s5, state])
