"""Unittesting of Weather classes

    Raises:
        ValueError: Tests if a value is actually populated
"""
from datetime import datetime, timezone
import pytz  # type: ignore
from typing import Any, Dict, Tuple, List
import random_address
import unittest
from unittest.mock import patch
from io import StringIO
from hypothesis import given, settings, strategies as st, Verbosity
from geolocation_api import GeoLocation
from weather_api import WeatherAPI
from main import WeatherAppMain, WeatherData
from geopy.geocoders import Nominatim


def convert_to_datetime(tz: str, utc_num: float, frmt_opt: int) -> Any:
    """Converts a UTC timestamp to a human-readable format
    using datetime. Then formats it for specific values within
    the JSON file

    Args:
        utc_num (float): UTC timestamp from JSON file
        frmt_opt (int): Formatting option for specific JSON values

    Returns:
        Any: Formatted string depending on the option that was
        used ex: Tues 1 March, 2024 7:34 PM MST-000 for 0 and
        7:34 PM MST-000 for anything else
    """
    if frmt_opt == 0:
        fmt = '%a %-d %B, %Y %-I:%M %p %Z%z'
    else:
        fmt = '%-I:%M %p %Z%z'
    utc_dt = datetime.fromtimestamp(utc_num, tz=timezone.utc)
    loc_tz = pytz.timezone(tz)
    loc_dt = loc_tz.normalize(utc_dt.astimezone(loc_tz))
    return loc_dt.strftime(fmt)


class TestWeatherAPI(unittest.TestCase):
    """Class to test weather modules

    Args:
        unittest (_type_): unittest module
    """

    def setUp(self) -> None:
        """Sets up the class instance variables for use with
        unittesting
        """
        self.w_api: WeatherAPI = WeatherAPI()
        self.geopy = Nominatim(user_agent='WeatherApp')
        self.geopy_api = GeoLocation()
        self.main = WeatherAppMain()
        self.data = WeatherData(
            loc=('39.7420', '-104.9915'),
            location="Denver, CO"
        )

    @given(
        st.builds(
            dict,
            **{
                key: st.just(value) for key, value in
                random_address.real_random_address().items()
            }
        )
    )
    @settings(
        deadline=None,
        verbosity=Verbosity.normal,
        max_examples=10
    )
    def test_api_call(self, ad_dict: Dict[str, Any]) -> None:
        """Gathers a dictionary from random_address module to
        be used to test if the api call is working properly

        Args:
            ad_dict (Dict[str, Any]): passed in dictionary
            from hypothesis

        """
        coord: Dict[str, Any] | None = ad_dict.get('coordinates')
        if coord is not None:
            coord_tuple: Tuple[str, str] | None = \
                (str(coord.get('lat')), str(coord.get('lng')))

            if coord_tuple is not None:
                self.w_api = WeatherAPI(coord_tuple)
                response = self.w_api.weather_api_call()

                cod: int | None = response.get('cod')
                self.assertEqual(cod, None)
        else:
            raise ValueError("Undefined Coordinate Tuple")  # pragma: no cover

    @given(
        st.builds(
            dict,
            **{
                key: st.just(value) for key, value in
                random_address.real_random_address().items()
            }
        )
    )
    @settings(
        deadline=None,
        verbosity=Verbosity.normal,
        max_examples=10
    )
    def test_geopy(self, ad_dict: Dict[str, Any]) -> None:
        """Uses the same strategy as test_api but tests against
        the GeoLocation module

        Args:
            ad_dict (Dict[str, Any]): passed in dictionary

        """
        address: str | None = ad_dict.get('address1')

        if address is not None:
            ad: Any = self.geopy.geocode(address)
            address1: Tuple[str, str] = (str(ad.latitude), str(ad.longitude))
            self.geopy_api.lat_lon_lookup(address)
            address2: Tuple[str, str] = self.geopy_api.user_loc
            self.assertEqual(address1, address2)
        else:
            raise ValueError("Undefined Address")  # pragma: no cover

    def test_main_app(self) -> None:
        """Test entire program run
        """
        with patch('sys.stdin', new=StringIO('Grand Junction, CO\n')):
            try:
                self.main.main()
            except Exception as e:  # pragma: no cover
                self.fail(f'Exception raised {e}')  # pragma: no cover

    def test_geolocation(self) -> None:
        """Tests GeoLocation module
        """
        with patch('sys.stdin', new=StringIO('Paonia, CO\n')):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.geopy_api.main()
                actual_ans = mock_stdout.getvalue().strip()

        coord: Any = self.geopy.geocode("Paonia, CO")
        expected_ans: Tuple[str, str] = (
            str(coord.latitude),
            str(coord.longitude)
        )
        self.assertEqual(str(expected_ans), actual_ans)

    def test_weatherapi(self) -> None:
        """Tests if the error printing function is
        working properly
        """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            cod_error: Dict[str, Any] = {
                "cod": 400,
                "message": "Invalid date format",
                "parameters": [
                    "date"
                ]
            }
            self.w_api.separate_lists(cod_error)
            expected_output = "Invalid date format status code: 400\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_main_alerts(self) -> None:
        """Tests Alerts function and if it is properly
        outputting

        Raises:
            ValueError: Undefined value
        """
        test_dict: Dict[str, Any] = {
            'alerts': [
                {
                    "sender_name": "Sender Name",
                    "event": "Event Name",
                    "start": 1684952747,
                    "end": 1684988747,
                    "description": "Alert Description",
                }
            ]
        }
        test_alerts: List[Dict[str, Any]] | None = test_dict.get('alerts')
        if test_alerts is None:
            raise ValueError("Test Alert was Undefined")
        s_utc: str = ""
        e_utc: str = ""
        for ta in test_alerts:
            s_utc += str(ta.get('start'))
            e_utc += str(ta.get('end'))
        timezone: str = "America/Denver"
        start_time: Any = convert_to_datetime(timezone, float(s_utc), 0)
        end_time: Any = convert_to_datetime(timezone, float(e_utc), 0)

        self.data.api.alerts = test_dict.get('alerts')  # type: ignore
        self.data.api.timezone_loc = "America/Denver"

        with patch.object(self.data, 'print_panel') as mock_panel:
            # self.w_api.alerts = test_dict.get('alerts')
            self.data.weather_alerts()
            mock_panel.assert_called_once_with(
                f"[b]Alert Sender:[/] Sender Name\n"
                f"[b]Event Name:[/] Event Name\n"
                f"[b]Start Time:[/] {start_time}\n"
                f"[b]End Time:[/] {end_time}\n"
                f"[b]Alert Description:[/] Alert Description\n",
                f"[b]Advisory Alerts for {self.data.location}[/]\n",
                None
            )

    def test_main_alerts2(self) -> None:
        """Tests if that the Alerts method is printing
        the correct output with an empty dictionary
        """
        test_dict: Dict[str, Any] = {}
        self.data.api.alerts = test_dict.get('alerts')  # type: ignore
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.data.weather_alerts()
            expected_ans: str = \
                f"No Weather Advisories for {self.data.location}\n"
            actual_ans = mock_stdout.getvalue()
        self.assertEqual(expected_ans, actual_ans)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
