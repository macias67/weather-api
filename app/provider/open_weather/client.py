from typing import Any

import requests

from app.provider.provider_interface import ProviderInterface
from app.settings import WEATHER_API_KEY, BASE_URL


class Client(ProviderInterface):
    def __init__(self, client_http=requests) -> None:
        self.client_http = client_http

    def fetch_info(self, city_name: str) -> Any:
        status_code = 0
        try:
            response = self.client_http.get(
                BASE_URL + "/data/2.5/forecast",
                params={"q": city_name, "cnt": 4, "lang": "es", "units": "metric", "appid": WEATHER_API_KEY},
                headers={'Accept': 'application/json'}
            )
            status_code = response.status_code
            response.raise_for_status()
        except requests.HTTPError:
            raise SystemExit("HTTP error, status code {}".format(status_code))
        except requests.RequestException as err:
            raise SystemExit("Ops, something went wrong... {}".format(err))

        return response.json()
