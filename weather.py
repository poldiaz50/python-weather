from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Cali"):
    requests_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"
    weather_data = requests.get(requests_url).json()
    return weather_data


if __name__ == "__main__":
    print("\n*** Obtener condiciones climaticas ***\n")
    city = input("\nPor favor ingresar el nombre de la ciutdad: ")
    # check para una cadena vacia
    if not bool(city.strip()):
        city = "santiago de cali"
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
