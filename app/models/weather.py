from dataclasses import dataclass


@dataclass
class Weather:
    id_weather: int
    main: str
    description: str

    def __init__(self, id_weather: int, main: str, description: str) -> None:
        self.id_weather = id_weather
        self.main = main
        self.description = description


@dataclass
class WeatherHour:
    dt_txt: str
    temp: float
    temp_min: float
    temp_max: float
    humidity: int
    weather: Weather

    def __init__(self, dt_txt: str, temp: float, temp_min: float, temp_max: float, humidity: int, weather: Weather):
        self.dt_txt = dt_txt
        self.temp = temp
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.humidity = humidity
        self.weather = weather
