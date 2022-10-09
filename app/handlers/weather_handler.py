from app.services.weather.weather_service import WeatherService

WEATHER_SERVICE = WeatherService()


def get_weather_by_city(city_name: str):
    return WEATHER_SERVICE.get_citi_weather(city_name)
