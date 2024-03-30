import sys
from typing import Tuple, Any
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


class GeoLocation():
    __user_lat: str
    __user_lon: str
    __user_loc: Nominatim = Nominatim(user_agent='WeatherApp')

    def __init__(
        self,
        default_lat='39.7420',
        default_lon='-104.9915'
            ) -> None:
        # Defaults to Denver, CO
        self.__user_lat = default_lat
        self.__user_lon = default_lon

    @property
    def user_loc(self) -> Tuple[str, str]:
        return self.__user_lat, self.__user_lon

    @user_loc.setter
    def user_loc(self, latlon: Tuple) -> None:
        self.__user_lat = str(latlon[0])
        self.__user_lon = str(latlon[1])

    def lat_lon_lookup(self, address: str) -> None:
        try:
            location = self.__user_loc.geocode(query=address)
            if location is None:
                raise ValueError("Address was not found using default")
        except ValueError as e:
            print(e)
        except GeocoderTimedOut as e:
            print(f"Session timed out {e}")
        except Exception as e:
            print(f"An error has occurred {e}")
        else:
            self.user_loc = (location.latitude, location.longitude)

    def print_user_loc(self) -> None:
        print(f'{self.user_loc}')

    @staticmethod
    def get_input(file: Any) -> str:
        file.stdout.write('Enter an address splitting with a ,: ')
        address = file.stdin.readline().rstrip()
        return address

    @staticmethod
    def main() -> None:
        geolocation = GeoLocation()
        address = geolocation.get_input(sys)
        geolocation.lat_lon_lookup(address)
        geolocation.print_user_loc()


if __name__ == "__main__":
    GeoLocation.main()
