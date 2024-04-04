"""Class that handles the actual API call to
https://openweathermap.org to retrieve JSON data
for output

    Returns:
        None
"""
import requests  # type: ignore
from typing import List, Tuple, Any, Dict
import config


class WeatherAPI:
    """Handles the API call and stores the returned
    data from the website

    Returns:
        None
    """
    __curr_weather: Dict[str, Any]
    __daily_weather: List[Dict[str, Any]]
    __alerts: List[Dict[str, Any]]
    __cod_error: Dict[str, Any]
    __api_key: str
    __timezone: str

    def __init__(
        self,
        user_loc: Tuple[str, str] = ('39.7420', '-104.9915')
    ) -> None:
        """Initilizes the user specified location using lat
        and lon of a specific address or defaults if none
        provided. And the API key that is stored elsewhere

        Args:
            user_loc (Tuple[str, str], optional):
            Latitude and Longitude to be used
            Defaults to ('39.7420', '-104.9915').
        """
        self.user_loc = user_loc
        self.__api_key = config.API_KEY

    @property
    def current_weather(self) -> Dict[str, Any]:
        """Getter function to get the current weather
        data

        Returns:
            Dict[str, Any]: Dictionary that holds
            current weather data
        """
        return self.__curr_weather

    @current_weather.setter
    def current_weather(self, curr_weather: Dict[str, Any]) -> None:
        """Sets the current weather dictionary to supplied values

        Args:
            curr_weather (Dict[str, Any]): Dictionary holding
            current weather data
        """
        self.__curr_weather = curr_weather

    @property
    def daily_weather(self) -> List[Dict[str, Any]]:
        """Getter function for daily weather data as a
        list of dictionary values

        Returns:
            List[Dict[str, Any]]: List of dictionary values
        """
        return self.__daily_weather

    @daily_weather.setter
    def daily_weather(self, daily_weather: List[Dict[str, Any]]) -> None:
        """Setter function to set daily weather with supplied data

        Args:
            daily_weather (List[Dict[str, Any]]): Supplied data
        """
        self.__daily_weather = daily_weather

    @property
    def alerts(self) -> List[Dict[str, Any]]:
        """Getter function for alerts data

        Returns:
            List[Dict[str, Any]]: List of dictionary values
            containing alerts
        """
        return self.__alerts

    @alerts.setter
    def alerts(self, weather_alerts: List[Dict[str, Any]]) -> None:
        """Setter function to set alerts data

        Args:
            weather_alerts (List[Dict[str, Any]]): data containing
            weather alerts
        """
        self.__alerts = weather_alerts

    @property
    def timezone_loc(self) -> str:
        """Getter function for timezone value

        Returns:
            str: timezone string
        """
        return self.__timezone

    @timezone_loc.setter
    def timezone_loc(self, tz: str) -> None:
        """Timzone setter function

        Args:
            tz (str): supplied timezone string
        """
        self.__timezone = tz

    @property
    def cod_error(self) -> Dict[str, Any]:
        """Getter function for error data

        Returns:
            Dict[str, Any]: Error data
        """
        return self.__cod_error

    @cod_error.setter
    def cod_error(self, errors: Dict[str, Any]) -> None:
        """Setter function for the error data from API call

        Args:
            errors (Dict[str, Any]): Error Data
        """
        self.__cod_error = errors

    @property
    def api_key(self) -> str:
        """API key for https://openweathermap.org API calls

        Returns:
            str: API key
        """
        return self.__api_key

    def weather_api_call(self) -> Any:
        """Sets up the url with specific parameters then calling
        the site passing in the parameters. Then checking if
        the response was good and returning that JSON data

        Returns:
            Any: JSON data that was retrieved from requests or
            a status code to raise and error
        """
        url = \
            "https://api.openweathermap.org/data/3.0/onecall?" \
            f"lat={self.user_loc[0]}&lon={self.user_loc[1]}&" \
            f"exclude=minutely,hourly&units=imperial&appid={self.api_key}"

        response = requests.get(url)

        if response.ok:
            return response.json()
        else:
            return response.status_code  # pragma: no cover

    def set_weather_data(self) -> None:
        """Calls the API fucntion to call the actual API
        then checks if the response was good or not
        """
        response = self.weather_api_call()

        if response:
            self.separate_lists(response)
        else:
            print(
                f"Error processing request, status code: {response}"
            )  # pragma: no cover

    def separate_lists(self, response: Any) -> None:
        """Seperates the data stored in the response variable to
        the appropriate class attributes

        Args:
            response (Any): Dictionary containg specific data
        """
        cod: int | None = response.get('cod')
        if cod is None:
            self.timezone_loc = response.get("timezone")
            self.current_weather = response.get("current")
            self.daily_weather = response.get("daily")
            self.alerts = response.get("alerts")
        else:
            self.cod_error = response
            self.print_errors()

    def print_errors(self) -> None:
        """For printing errors and exiting program
        """
        errors: Dict[str, Any] | None = self.cod_error
        if errors is not None:
            cod: int | None = errors.get('cod')
            msg: str | None = errors.get('message')

            if cod and msg is not None:
                print(f"{msg} status code: {cod}")


if __name__ == "__main__":
    app = WeatherAPI()  # pragma: no cover
    app.set_weather_data()  # pragma: no cover
