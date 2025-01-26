import asyncio
import datetime
from baml_client import b
from baml_client.types import WeatherAPI

def get_weather(city: str, time_of_day: datetime.date):
    ...

def main():
    weather_info = b.UseTool("What's the weather like in San Francisco?")
    print(weather_info)
    assert isinstance(weather_info, WeatherAPI)
    print(f"City: {weather_info.city}")
    print(f"Time of Day: {weather_info.time_of_day}")
    weather = get_weather(city=weather_info.city, time_of_day=weather_info.timeOfDay)

if __name__ == '__main__':
    main()
