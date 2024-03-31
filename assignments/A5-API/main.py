import sys
from typing import Any, Tuple
from rich import print
from geolocation_api import GeoLocation
from weather_api import WeatherAPI


class WeatherAppMain:
    def __init__(self) -> None:
        self.geo_loc = GeoLocation()

    def lookup(self, location: str) -> None:
        self.geo_loc.lat_lon_lookup(location)

    @property
    def loc(self) -> Tuple[str, str]:
        return self.geo_loc.user_loc

    @staticmethod
    def user_input(file: Any) -> str:
        print(
            "[bright white]"
            "Enter a location separated by a ,: "
            "[/bright white]")
        location: str = file.readline().rstrip()
        return location

    @staticmethod
    def main() -> None:
        wam = WeatherAppMain()
        location = wam.user_input(sys.stdin)
        wam.lookup(location)


class WeatherData(WeatherAppMain):
    def __init__(self) -> None:
        super().__init__()
        self.api = WeatherAPI(self.loc)

    def call_api(self) -> None:
        pass


if __name__ == "__main__":
    WeatherAppMain.main()
