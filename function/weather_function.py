import requests
import json
import os
from datetime import datetime


class WeatherSampler:

    def __init__(self, api_key):
        self.api_key = api_key
        self.geo_url = "http://api.openweathermap.org/geo/1.0/direct"
        self.weather_url = "https://api.openweathermap.org/data/2.5/weather"

    def getTimestampGmt7(self):
        now_utc = datetime.utcnow()
        gmt7 = now_utc.timestamp() + (7 * 3600)
        local_time = datetime.fromtimestamp(gmt7)
        return local_time.strftime("%Y-%m-%d %H:%M:%S")

    def getLatLon(self, city_name):
        params = {
            "q": city_name,
            "limit": 1,
            "appid": self.api_key
        }

        response = requests.get(self.geo_url, params=params)

        if response.status_code == 200:
            data = response.json()
            if len(data) > 0:
                lat = data[0]["lat"]
                lon = data[0]["lon"]
                return lat, lon
            else:
                raise Exception(f"Kota '{city_name}' tidak ditemukan.")
        else:
            raise Exception(f"Failed get lat/lon: Status Code {response.status_code} - {response.text}")

    def sampleWeather(self, city_name):
        try:
            lat, lon = self.getLatLon(city_name)

            params = {
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": "metric"
            }

            response = requests.get(self.weather_url, params=params)

            if response.status_code == 200:
                data = response.json()

                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]

                # Save to JSON
                base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
                log_folder = os.path.join(os.getcwd(), "log")
                if not os.path.exists(log_folder):
                    os.makedirs(log_folder)

                result = {
                    "timestamp": self.getTimestampGmt7(),
                    "city": city_name,
                    "latitude": lat,
                    "longitude": lon,
                    "temperature": temp,
                    "temperature_unit": "Celsius",
                    "humidity": humidity,
                    "humidity_unit": "%"
                }

                try:
                    save_path = os.path.join(log_folder, "data_weather.json")
                    with open(save_path, "w") as json_file:
                        json.dump(result, json_file, indent=4)
                except Exception as e:
                    print(f"Failed to save JSON: {e}")

                # with open(os.path.join(log_folder, "data_weather.json"), "w") as json_file:
                #     json.dump(result, json_file, indent=4)

                print(f"{result['timestamp']} - Success Running Sampling Data Weather with Result Temperature {temp} Celsius & Humidity {humidity} %")

            else:
                timestamp = self.getTimestampGmt7()
                print(f"{timestamp} - Failed Running Sampling Data Weather with Status Code {response.status_code} - {response.text}")

        except Exception as e:
            timestamp = self.getTimestampGmt7()
            print(f"{timestamp} - Failed Running Sampling Data Weather - Exception: {e}")
