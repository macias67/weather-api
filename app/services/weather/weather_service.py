from app.models.city import City
from app.provider.open_weather.client import Client
from app.provider.provider_interface import ProviderInterface


class WeatherService:
    CLIENT_HTTP: ProviderInterface = Client()

    def get_citi_weather(self, city_name: str) -> City:
        weather_info = self.CLIENT_HTTP.fetch_info(city_name=city_name)
        city = City(weather_info)

        return city
