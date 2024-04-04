"""Main file that uses two classes, one for prompts
and calls to the data class. The other class being for
the initial API call and then processing and printing
of the returned weather data.

    Raises:
        ValueErrors: All the value errors are used for
        making sure that values are being passed in and
        not just failing at the first instance

    Returns:
        None
"""

from datetime import datetime, timezone
import pytz  # type: ignore
from typing import Tuple, Dict, Any, List, Optional
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
from geolocation_api import GeoLocation
from weather_api import WeatherAPI


class WeatherAppMain:
    """This class is used for prompting the user to enter
    in an address to look up specific weather data about.
    It uses the GeoLocation class to then search for the
    address and get the location coordinates and pass it to
    the WeatherData class
    """

    def __init__(self) -> None:
        """Initializes the Geopy module and the prompt
        class from Rich module
        """
        self.geo_loc = GeoLocation()
        self.prompt = Prompt()

    def lookup(self, location: str) -> None:
        """Function  to pass in the address that was
        supplied by the user and sets the GeoLocation
        lat and lon values to those found values

        Args:
            location (str): User entered address
        """
        self.geo_loc.lat_lon_lookup(location)

    @property
    def loc(self) -> Tuple[str, str]:
        """Getter function to access the tuple that
        contains the string representations of the lat
        and lon

        Returns:
            Tuple[str, str]: Tuple containing two strings lat and
            lon
        """
        return self.geo_loc.user_loc

    def user_input(self) -> str:
        """Function for getting user input for an address
        using the Prompt class from Rich module

        Returns:
            str: User entered address
        """
        location: str = \
            self.prompt.ask(
                "[chartreuse1]Enter a location separated by a ',' "
                "[/chartreuse1]")
        return location

    @staticmethod
    def main() -> None:
        """Main function that handles all the calls for this
        class and the WeatherData class
        """
        wam = WeatherAppMain()
        location = wam.user_input()
        wam.lookup(location)
        wd = WeatherData(wam.loc, location)
        wd.call_api()
        wd.current_weather_data()
        wd.daily_weather()
        wd.weather_alerts()


class WeatherData:
    """Processes the JSON data that is set in the WeatherAPI
    class and prints the data using the Panel class from Rich
    module
    """

    def __init__(
            self,
            loc: Tuple[str, str],
            location: str
    ) -> None:
        """Initializes the WeatherAPI class with the
        tuple containing the lat and lon. Along with
        the user supplied address

        Args:
            loc (Tuple[str, str]): Latitude and Longitude values
            location (str): User supplied address
        """
        self.api = WeatherAPI(loc)
        self.location = location

    def call_api(self) -> None:
        """Simple function that just calls the WeatherAPI
        class and sets the JSON data within that class
        """
        self.api.set_weather_data()

    def convert_to_datetime(self, utc_num: float, frmt_opt: int) -> Any:
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
        utc_dt = datetime.fromtimestamp(timestamp=utc_num, tz=timezone.utc)
        loc_tz = pytz.timezone(self.api.timezone_loc)
        loc_dt = loc_tz.normalize(utc_dt.astimezone(loc_tz))
        return loc_dt.strftime(fmt)

    @staticmethod
    def print_panel(
            output_str: str,
            title: str | None,
            subtitle: str | None
    ) -> None:
        """Prints out the passed in concatenated string along with
        the title and subtitle, using Panel class

        Args:
            output_str (str): Concatenated string
            title (str): Title for Panel output
            subtitle (str): Subtitle for Panel output
        """
        if title and subtitle is not None:
            panel = Panel(
                output_str,
                title=title,
                title_align='center',
                subtitle=subtitle,
                subtitle_align='center'
            )
        elif subtitle is None:
            panel = Panel(
                output_str,
                title=title,
                title_align='center'
            )
        elif title is None:  # pragma: no cover
            panel = Panel(
                output_str,
                subtitle=subtitle,
                subtitle_align='center'
            )
        else:  # pragma: no cover
            panel = Panel(
                output_str
            )
        print(panel)

    def current_weather_data(self) -> None:  # noqa: C901
        """Process the data returned from WeatherAPI that
        stores the JSON values. As well as concatenates a
        string of all the different data values

        Raises:
            ValueError: All value errors are just for checking
            if a value is in there and flagging the program if
            it is not
        """
        curr_w = self.api.current_weather

        if curr_w.get('dt') is not None:
            curr_time = \
                self.convert_to_datetime(float(str(curr_w.get('dt'))), 0)
        else:
            raise ValueError('Date Time is Undefined')

        if curr_w.get('sunrise') is not None:
            curr_sunrise = \
                self.convert_to_datetime(float(str(curr_w.get('sunrise'))), 1)
        else:
            raise ValueError('Sunrise is Undefined')

        if curr_w.get('sunset') is not None:
            curr_sunset = \
                self.convert_to_datetime(float(str(curr_w.get('sunset'))), 1)
        else:
            raise ValueError('Sunset is Undefined')  # pragma: no cover

        subtitle = f"[b]Current Weather for {self.location}[/]"
        title = f"[b]{curr_time}[/]"
        curr_w_output = f"[b]Sunrise:[/] {curr_sunrise}\n"
        curr_w_output += f"[b]Sunset:[/] {curr_sunset}\n"

        description: List[Dict[str, Any]]
        weather_data: Optional[List[Dict[str, Any]]] = curr_w.get('weather')
        if weather_data is not None:
            description = weather_data
            for desc in description:
                main = desc.get('main')
                main_desc = desc.get('description')
                if main and main_desc:
                    curr_w_output += \
                        f"[b]Description:[/] {main} - {main_desc}\n"
        else:
            raise ValueError('Empty Weather Data List')  # pragma: no cover

        curr_w_output += \
            f"[b]Temperature:[/] {curr_w.get('temp')}\N{DEGREE SIGN}F " \
            f"[b]Feels like:[/] {curr_w.get('feels_like')}\N{DEGREE SIGN}F\n"
        curr_w_output += f"[b]Humidity:[/] {curr_w.get('humidity')}%\n"
        curr_w_output += f"[b]Cloudiness:[/] {curr_w.get('clouds')}%\n"
        curr_w_output += f"[b]UV Index:[/] {curr_w.get('uvi')}\n"

        v_str: str | None = curr_w.get('visibility')
        if v_str is not None:
            v_float: float = float(v_str)
            curr_w_output += (
                f"[b]Visibility:[/] "
                f"{(v_float * 3.28):.2f} "
                f"Foot/Feet\n"
            )
        else:
            raise ValueError('Visibility is Undefined')

        curr_w_output += f"[b]Wind Speed:[/] {curr_w.get('wind_speed')}mph\n"

        if curr_w.get('wind_gust') is not None:
            curr_w_output += \
                f"[b]Wind Gusts:[/] {curr_w.get('wind_gust')}mph\n"

        curr_rain: Dict[str, Any] | None = curr_w.get('rain')
        if curr_rain is not None:
            curr_w_output += \
                f"[b]Current Precipitation:[/] " \
                f"{float(str(curr_rain.get('1h'))) / 25.4}\n" \
                # pragma: no cover

        curr_snow: Dict[str, Any] | None = curr_w.get('snow')
        if curr_snow is not None:
            curr_w_output += \
                f"[b]Current Snow Accumulation:[/] " \
                f"{float(str(curr_snow.get('1h'))) / 25.4}\n" \
                # pragma: no cover

        self.print_panel(curr_w_output, title, subtitle)

    def daily_weather(self) -> None:  # noqa: C901
        """Function that processes the data from a list of
        dictionary values retrieved from the WeatherAPI class
        then does the same as the current_weather function

        Raises:
            ValueError: If value is none
        """
        for dw in self.api.daily_weather:
            if dw.get('dt') is not None:
                dt = \
                    self.convert_to_datetime(float(str(dw.get('dt'))), 0)

            if dw.get('sunrise') is not None:
                sr = \
                    self.convert_to_datetime(
                        float(str(dw.get('sunrise'))),
                        1
                    )

            if dw.get('sunset') is not None:
                sst = \
                    self.convert_to_datetime(
                        float(str(dw.get('sunset'))),
                        1
                    )

            if dw.get('moonrise') is not None:
                mr = \
                    self.convert_to_datetime(
                        float(str(dw.get('moonrise'))),
                        1
                    )

            if dw.get('moonset') is not None:
                mst = \
                    self.convert_to_datetime(
                        float(str(dw.get('moonset'))),
                        1
                    )

            title = f"[b]{dt}[/]"
            subtitle = f"[b]Daily Weather Updates for {self.location}[/]"

            dw_output = ""
            dw_output += f"[b]Summary:[/] {dw.get('summary')}\n"
            dw_output += f"[b]Sunrise:[/] {sr}\n"
            dw_output += f"[b]Sunset:[/] {sst}\n"
            dw_output += f"[b]Moonrise:[/] {mr}\n"
            dw_output += f"[b]Moonset:[/] {mst}\n"
            dw_output += f"[b]Moon Phase:[/] {dw.get('moon_phase')}\n"
            dw_output += (
                f"[b]Daily Temp[/]\n[b]Morning Temp:[/] "
                f"{dw['temp'].get('morn')}"
                f"\N{DEGREE SIGN}F [b]Day Temp:[/] {dw['temp'].get('day')}"
                f"\N{DEGREE SIGN}F [b]Evening Temp:[/] "
                f"{dw['temp'].get('eve')}"
                f"\N{DEGREE SIGN}F [b]Night Temp:[/] "
                f"{dw['temp'].get('night')}"
                f"\N{DEGREE SIGN}F\n [b]Min Daily Temp:[/] "
                f"{dw['temp'].get('min')}"
                f"\N{DEGREE SIGN}F [b]Max Daily Temp:[/] "
                f"{dw['temp'].get('max')}"
                f"\N{DEGREE SIGN}F\n"
            )
            dw_output += (
                f"[b]Daily Feels Like[/]\n[b]Morning Temp:[/] "
                f"{dw['feels_like'].get('morn')}\N{DEGREE SIGN}F "
                f"[b]Day Temp:[/] "
                f"{dw['feels_like'].get('day')}\N{DEGREE SIGN}F "
                f"[b]Evening Temp:[/] "
                f"{dw['feels_like'].get('eve')}\N{DEGREE SIGN}F"
                f" [b]Night Temp:[/] {dw['feels_like'].get('night')}"
                f"\N{DEGREE SIGN}F\n"
            )
            dw_output += f"[b]Humidity:[/] {dw.get('humidity')}%\n"
            dw_output += f"[b]Wind Speed:[/] {dw.get('wind_speed')}mph\n"

            if dw['wind_gust']:
                dw_output += f"[b]Wind Gusts:[/] {dw.get('wind_gust')}mph\n"

            dw_output += \
                f"[b]Wind Direction:[/] " \
                f"{dw.get('wind_deg')}\N{DEGREE SIGN}\n"
            dw_output += f"[b]Cloudiness:[/] {dw.get('clouds')}%\n"
            dw_output += f"[b]UV Index:[/] {dw.get('uvi')}\n"

            pop: float | None = dw.get('pop')
            if pop is not None:
                dw_output += \
                    f"[b]Probability of Precipitation:[/] " \
                    f"{pop * 100}%\n"

            if dw.get('rain') is not None:
                dw_output += \
                    f"[b]Preciptation Volume:[/] " \
                    f"{dw.get('rain')} inch/hour\n"

            if dw.get('snow') is not None:
                dw_output += \
                    f"[b]Snow Accumulation:[/] {dw.get('snow')} inch/hour\n" \
                    # pragma: no cover

            description: List[Dict[str, Any]]
            weather_data: Optional[List[Dict[str, Any]]] = dw.get('weather')
            if weather_data is not None:
                description = weather_data
                for desc in description:
                    main = desc.get('main')
                    main_desc = desc.get('description')
                    if main and main_desc:
                        dw_output += \
                            f"[b]Description:[/] {main} - {main_desc}\n"
            else:
                raise ValueError('Empyt Weather Data List'
                                 )  # pragma: no cover

            self.print_panel(dw_output, title, subtitle)

    def weather_alerts(self) -> None:
        """This does the same as the previous function
        that gets a list of dictionary values and concatenates
        it into a string to be output
        """
        alerts = self.api.alerts

        if alerts:
            for aa in alerts:
                title = f"[b]Advisory Alerts for {self.location}[/]\n"
                aa_output = f"[b]Alert Sender:[/] {aa.get('sender_name')}\n"
                aa_output += f"[b]Event Name:[/] {aa.get('event')}\n"
                if aa.get('start') is not None:
                    start_time = \
                        self.convert_to_datetime(
                            float(str(aa.get('start'))),
                            0
                        )

                if aa.get('end') is not None:
                    end_time = \
                        self.convert_to_datetime(
                            float(str(aa.get('end'))),
                            0
                        )

                aa_output += f"[b]Start Time:[/] {start_time}\n"
                aa_output += f"[b]End Time:[/] {end_time}\n"
                aa_output += \
                    f"[b]Alert Description:[/] {aa.get('description')}\n"

                self.print_panel(aa_output, title, None)
        else:
            print(f"No Weather Advisories for {self.location}")


if __name__ == "__main__":
    WeatherAppMain.main()  # pragma: no cover
