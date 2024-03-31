# import json
import requests
from typing import List, Tuple, Any
# from main import WeatherAppMain
import config


class WeatherAPI:
    __curr_weather: List
    __daily_weather: List
    __alerts: List
    __api_key: str

    def __init__(self, user_loc: Tuple = ('39.7420', '-104.9915')) -> None:
        self.user_loc = user_loc
        self.__api_key = config.API_KEY

    @property
    def current_weather(self) -> List[Any]:
        return self.__curr_weather

    @current_weather.setter
    def current_weather(self, curr_weather: List[Any]) -> None:
        self.__curr_weather = curr_weather

    @property
    def daily_weather(self) -> List[Any]:
        return self.__daily_weather

    @daily_weather.setter
    def daily_weather(self, daily_weather: List[Any]) -> None:
        self.__daily_weather = daily_weather

    @property
    def alerts(self) -> List[Any]:
        return self.__alerts

    @alerts.setter
    def alerts(self, weather_alerts: List[Any]) -> None:
        self.__alerts = weather_alerts

    @property
    def api_key(self) -> str:
        return self.__api_key

    def weather_api_call(self) -> Any:
        url = \
            "https://api.openweathermap.org/data/3.0/onecall?" \
            f"lat={self.user_loc[0]}&lon={self.user_loc[1]}&" \
            f"exclude=minutely,hourly&units=imperial&appid={self.api_key}"
        # url = \
        #     "https://api.openweathermap.org/data/3.0/onecall?" \
        #     "lat=39.7420&lon=-104.9915&" \
        #     f"exclude=minutely,hourly&units=imperial&appid={self.api_key}"

        response = requests.get(url)

        if response.ok:
            return response.json()
        else:
            return response.status_code

    def set_weather_data(self) -> None:
        response = self.weather_api_call()
        # print(f"{type(response)}\n{response}")

        if response:
            self.separate_lists(response)
        else:
            response.raise_for_status()

    def separate_lists(self, response: Any) -> None:
        self.current_weather = response.get("current")
        self.daily_weather = response.get("daily")
        self.alerts = response.get("alert")
        # self.print_attributes()

    def print_attributes(self) -> None:
        print(f"{self.current_weather}\n{self.daily_weather}\n{self.alerts}")


class CurrentWeather(WeatherAPI):
    def __init__(self, user_loc: Tuple[str]) -> None:
        super().__init__(user_loc)


class DailyWeather(WeatherAPI):
    def __init__(self, user_loc: Tuple[str]) -> None:
        super().__init__(user_loc)


class AdvisoryAlerts(WeatherAPI):
    def __init__(self, user_loc: Tuple[str]) -> None:
        super().__init__(user_loc)


if __name__ == "__main__":
    app = WeatherAPI()
    app.set_weather_data()
