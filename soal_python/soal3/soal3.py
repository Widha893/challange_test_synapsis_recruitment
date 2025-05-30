from function.weather_function import WeatherSampler
import time


def getUserInterval():
    while True:
        user_input = input("Masukkan interval sampling (detik, > 0): ")
        try:
            interval = int(user_input)
            if interval > 0:
                return interval
            else:
                print("Input harus angka di atas 0!")
        except ValueError:
            print("Input harus angka di atas 0!")


if __name__ == "__main__":

    API_KEY = "64578d113bb9b9dc0f7d657574ccdcab"

    weather_sampler = WeatherSampler(API_KEY)

    city = input("Masukkan nama kota: ")

    interval = getUserInterval()

    print(f"\nMemulai sampling data weather untuk kota '{city}' setiap {interval} detik...\n")

    while True:
        weather_sampler.sampleWeather(city)
        time.sleep(interval)
