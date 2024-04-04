"""Uses the geopy.geocoders API to convert an address that a user
provides and stores as a string for later use

    Raises:
        ValueError: If the address when ran through the gecoders
        API does not return a valid value. Output message and use
        default values

    Returns:
        None
"""

import sys
from typing import Tuple, Any
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


class GeoLocation():
    """Class that is used to call Geopy API and store
    latitude and longitude as a string values inside a
    tuple

    Returns:
        None
    """
    __user_lat: str
    __user_lon: str
    __user_loc: Nominatim = Nominatim(user_agent='WeatherApp')

    def __init__(
        self,
        default_lat: str = '39.7420',
        default_lon: str = '-104.9915'
    ) -> None:
        """Initilizes the class attibutes lat and lon to Denver, CO
        and then when the Geopy API is called it is updated with new
        values

        Args:
            default_lat (str, optional):
            Latitude value. Defaults to '39.7420'.

            default_lon (str, optional):
            Longitude value. Defaults to '-104.9915'.
        """
        # Defaults to Denver, CO
        self.__user_lat = default_lat
        self.__user_lon = default_lon

    @property
    def user_loc(self) -> Tuple[str, str]:
        """Getter function for tuple that contains the string
        representations of latitude and longitude values

        Returns:
            Tuple[str, str]: For access of private attribute values
        """
        return self.__user_lat, self.__user_lon

    @user_loc.setter
    def user_loc(self, latlon: Tuple[str, str]) -> None:
        """Setter function that sets the tuple with the string
        representation of latitude and longitude

        Args:
            latlon (Tuple[str, str]): Tuple that contains the lat
            and long
        """
        self.__user_lat = str(latlon[0])
        self.__user_lon = str(latlon[1])

    def lat_lon_lookup(self, address: str) -> None:
        """Calls the Geopy geocoder API with the user-supplied
        address to get the coordinates of the location

        Args:
            address (str): User supplied address

        Raises:
            ValueError: If the address is not valid then
            state that it was not and use default values
        """
        try:
            location = self.__user_loc.geocode(query=address)
            if location is None:
                raise ValueError(
                    "Address was not found using default")  # pragma: no cover
        except ValueError as e:  # pragma: no cover
            print(e)
        except GeocoderTimedOut as e:  # pragma: no cover
            print(f"Session timed out {e}")
        except Exception as e:  # pragma: no cover
            print(f"An error has occurred {e}")
        else:
            self.user_loc = (location.latitude, location.longitude)

    def print_user_loc(self) -> None:
        """Print function that was used for testing
        """
        print(f'{self.user_loc}')

    @staticmethod
    def get_input(file: Any) -> str:
        """Uses system functions to get input from user
        through the command line. Returning a string of
        an address. This was used for testing and not
        for the actual code.

        Args:
            file (Any): Sys module for command line fucntions

        Returns:
            str: The address that the user wants to look up geopy
            data for
        """
        address: str = file.stdin.readline().rstrip()
        return address

    @staticmethod
    def main() -> None:
        """Main function that was used for testing purposes
        """
        geolocation = GeoLocation()
        address = geolocation.get_input(sys)
        geolocation.lat_lon_lookup(address)
        geolocation.print_user_loc()


if __name__ == "__main__":
    GeoLocation.main()  # pragma: no cover
