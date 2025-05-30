from function.mqtt_function import MqttPublisher
import paho.mqtt.client as mqtt
import time

class MqttApp:

    def __init__(self):
        # Setting kandidat name + topic
        self.kandidat_name = "Widha"
        self.mqtt_topic = f"mqtt/{self.kandidat_name}/data"

        # Setup MQTT client
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect("test.mosquitto.org", 1883, 60)

        # Create publisher object
        self.publisher = MqttPublisher(self.mqtt_client, self.mqtt_topic, self.kandidat_name)

        # Default interval
        self.interval = 5

    def getUserInterval(self):
        while True:
            user_input = input("Masukkan interval publish (detik, > 0): ")
            try:
                interval = int(user_input)
                if interval > 0:
                    self.interval = interval
                    break
                else:
                    print("Anda harus menginputkan angka di atas 0!")
            except ValueError:
                print("Anda harus menginputkan angka di atas 0!")

    def run(self):
        print(f"\nMemulai publish ke MQTT setiap {self.interval} detik...\n")

        while True:
            self.publisher.publishData()
            self.mqtt_client.loop()
            time.sleep(self.interval)


if __name__ == "__main__":
    app = MqttApp()
    app.getUserInterval()
    app.run()
