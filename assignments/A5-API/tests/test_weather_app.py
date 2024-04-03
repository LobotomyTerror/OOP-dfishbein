# import os
# import json
from typing import Any, Dict
import random_address  # type: ignore
import unittest
# from unittest.mock import patch
# from io import StringIO
from hypothesis import given, settings, strategies as st, Verbosity
# from geolocation_api import GeoLocation
# from main import WeatherAppMain, WeatherData
# from weather_api import WeatherAPI


class TestWeatherAPI(unittest.TestCase):
    address_dict: Dict[str, Any] = random_address.real_random_address()

    @settings(
        deadline=None,
        derandomize=False,
        max_examples=50,
        verbosity=Verbosity.normal
    )
    @given(st.builds(
        dict,
        **{key: st.just(value) for key, value in address_dict.items()}
    ))
    def test_api(self, ad_dict: Any) -> None:
        print(ad_dict)


if __name__ == "__main__":
    unittest.main()
