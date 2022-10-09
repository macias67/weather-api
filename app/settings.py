from dotenv import dotenv_values

env = dotenv_values(".env.local")

BASE_URL = env["BASE_URL_WEATHER_API"]
WEATHER_API_KEY = env["WEATHER_API_KEY"]
