from datetime import datetime, timezone
import pytz
from typing import Tuple, Dict
from rich import print
from rich.live import Live
from rich.layout import Layout
from rich.prompt import Prompt
from rich.panel import Panel
from geolocation_api import GeoLocation
from weather_api import WeatherAPI


class WeatherAppMain:
    def __init__(self) -> None:
        self.geo_loc = GeoLocation()
        self.layout = Layout()
        self.prompt = Prompt()
        # self.live = Live()

    def lookup(self, location: str) -> None:
        self.geo_loc.lat_lon_lookup(location)

    def render_layout(self) -> Layout:
        self.layout.split_column(
            Layout(name="curr_weather", visible=False),
            Layout(name="daily_weather", visible=False),
            Layout(name="alerts", visible=False)
        )
        self.layout['curr_weather'].split_column(
            Layout(name='cw_details', size=12)
        )
        self.layout['cw_details'].split()

        self.layout['daily_weather'].split_column(
            Layout(name='dw_details')
        )
        self.layout['dw_details'].split()

        return self.layout

    @property
    def loc(self) -> Tuple[str, str]:
        return self.geo_loc.user_loc

    def user_input(self) -> str:
        location: str = \
            self.prompt.ask(
                "[chartreuse1]Enter a location seperated by a ',' "
                "[/chartreuse1]")
        return location

    @staticmethod
    def main() -> None:
        wam = WeatherAppMain()
        location = wam.user_input()
        wam.lookup(location)
        layout = wam.render_layout()
        with Live(auto_refresh=False, screen=True) as live:
            wd = WeatherData(wam.loc, layout, location)
            wd.call_api()
            live.update(wd.current_weather_data(), refresh=True)
            live.update(wd.daily_weather(), refresh=True)
            # wd.weather_alerts()


class WeatherData:
    def __init__(
            self, loc: Tuple[str, str],
            layout: Layout,
            location: str) -> None:

        self.api = WeatherAPI(loc)
        self.layout = layout
        self.location = location

    def call_api(self) -> None:
        self.api.set_weather_data()

    def convert_to_datetime(self, utc_num: float, frmt_opt: int) -> datetime:
        if frmt_opt == 0:
            fmt = '%a %d %B, %Y %-I:%M %p %Z%z'
        else:
            fmt = '%-I:%M %p %Z%z'
        utc_dt = datetime.fromtimestamp(timestamp=utc_num, tz=timezone.utc)
        loc_tz = pytz.timezone(self.api.timezone_loc)
        loc_dt = loc_tz.normalize(utc_dt.astimezone(loc_tz))
        return loc_dt.strftime(fmt)

    def current_weather_data(self) -> Layout:
        curr_w = self.api.current_weather
        curr_time = self.convert_to_datetime(float(curr_w.get('dt')), 0)
        curr_sunrise = \
            self.convert_to_datetime(float(curr_w.get('sunrise')), 1)
        curr_sunset = \
            self.convert_to_datetime(float(curr_w.get('sunset')), 1)

        subtitle = f"Current Weather for {self.location}"
        title = f"{curr_time}"
        curr_w_output = f"Sunrise: {curr_sunrise}\n"
        curr_w_output += f"Sunset: {curr_sunset}\n"

        description = curr_w.get('weather')
        for desc in description:
            main = desc.get('main')
            main_desc = desc.get('description')
            if main and main_desc:
                curr_w_output += f"Description: {main} - {main_desc}\n"

        curr_w_output += \
            f"Temperature: {curr_w.get('temp')}\N{DEGREE SIGN}F " \
            f"Feels like: {curr_w.get('feels_like')}\N{DEGREE SIGN}F\n"
        curr_w_output += f"Humidity: {curr_w.get('humidity')}%\n"
        curr_w_output += f"Cloudiness: {curr_w.get('clouds')}%\n"
        curr_w_output += f"UV Index: {curr_w.get('uvi')}\n"
        curr_w_output += \
            f"Visibility: {(curr_w.get('visibility') * 3.28):.2f} Foot/Feet\n"
        curr_w_output += f"Wind Speed: {curr_w.get('wind_speed')}mph\n"

        if curr_w.get('wind_gust') is not None:
            curr_w_output += \
                f"Wind Gusts: {curr_w.get('wind_gust')}mph\n"
        curr_rain: Dict = curr_w.get('rain')
        if curr_rain:
            curr_w_output += \
                f"Current Precipitation: {curr_rain.get('1h') / 25.4}\n"
        curr_snow: Dict = curr_w.get('snow')
        if curr_snow:
            curr_w_output += \
                f"Current Snow Accumulation: {curr_snow.get('1h') / 25.4}\n"

        self.layout['curr_weather'].visible = True
        self.layout['cw_details'].update(
            self.layout['cw_details'].add_split(
                    Panel(
                        curr_w_output,
                        title=title,
                        title_align='center',
                        subtitle=subtitle,
                        subtitle_align='center'
                    )
                )
            )
        return self.layout

    def daily_weather(self) -> Layout:
        self.layout['daily_weather'].visible = True

        for dw in self.api.daily_weather:
            dt = \
                self.convert_to_datetime(float(dw.get('dt')), 0)
            sr = \
                self.convert_to_datetime(float(dw.get('sunrise')), 1)
            sst = \
                self.convert_to_datetime(float(dw.get('sunset')), 1)
            mr = \
                self.convert_to_datetime(float(dw.get('moonrise')), 1)
            mst = \
                self.convert_to_datetime(float(dw.get('moonset')), 1)

            title = f"{dt}"
            subtitle = f"Daily Weather Updates for {self.location}"

            dw_output = ""
            dw_output += f"Summary: {dw.get('summary')}\n"
            dw_output += f"Sunrise: {sr}\n"
            dw_output += f"Sunset: {sst}\n"
            dw_output += f"Moonrise: {mr}\n"
            dw_output += f"Moonset: {mst}\n"
            dw_output += f"Moon Phase: {dw.get('moon_phase')}\n"
            dw_output += (
                f"Daily Temp\nMorning Temp: {dw['temp'].get('morn')}"
                f"\N{DEGREE SIGN}F Day Temp: {dw['temp'].get('day')}"
                f"\N{DEGREE SIGN}F Evening Temp: {dw['temp'].get('eve')}"
                f"\N{DEGREE SIGN}F Night Temp: {dw['temp'].get('night')}"
                f"\N{DEGREE SIGN}F\n Min Daily Temp: {dw['temp'].get('min')}"
                f"\N{DEGREE SIGN}F Max Daily Temp: {dw['temp'].get('max')}"
                f"\N{DEGREE SIGN}F\n"
            )
            dw_output += (
                f"Daily Feels Like\nMorning Temp: "
                f"{dw['feels_like'].get('morn')}\N{DEGREE SIGN}F "
                f"Day Temp: {dw['feels_like'].get('day')}\N{DEGREE SIGN}F "
                f"Evening Temp: {dw['feels_like'].get('eve')}\N{DEGREE SIGN}F"
                f" Night Temp: {dw['feels_like'].get('night')}"
                f"\N{DEGREE SIGN}F\n"
            )
            dw_output += f"Humidity: {dw.get('humidity')}%\n"
            dw_output += f"Wind Speed: {dw.get('wind_speed')}mph\n"

            if dw['wind_gust']:
                dw_output += f"Wind Gusts: {dw.get('wind_gust')}mph\n"

            dw_output += \
                f"Wind Direction: {dw.get('wind_deg')}\N{DEGREE SIGN}\n"
            dw_output += f"Cloudiness: {dw.get('clouds')}%\n"
            dw_output += f"UV Index: {dw.get('uvi')}\n"
            dw_output += \
                f"Probability of Precipitation: {dw.get('pop') * 100}%\n"

            if dw.get('rain') is not None:
                dw_output += \
                    f"Preciptation Volume: {dw.get('rain')} inch/hour\n"

            if dw.get('snow') is not None:
                dw_output += \
                    f"Snow Accumulation: {dw.get('snow')} inch/hour\n"

            description = dw.get('weather')
            for desc in description:
                main = desc.get('main')
                main_desc = desc.get('description')
                if main and main_desc:
                    dw_output += f"Description: {main} - {main_desc}\n"

            self.layout['daily_weather'].update(
                self.layout['dw_details'].update(
                    self.layout['dw_details'].add_split(
                        Panel(
                            dw_output,
                            title=title,
                            title_align='center',
                            subtitle=subtitle,
                            subtitle_align='center'
                        )
                    )
                )
            )
        return self.layout['daily_weather']

    def weather_alerts(self) -> None:
        alerts = self.api.alerts

        if alerts:
            for aa in alerts:
                aa_output = f"Advisory Alerts for {self.location}\n"
                aa_output += f"Alert Sender: {aa.get('sender_name')}\n"
                aa_output += f"Event Name: {aa.get('event')}\n"
                start_time = \
                    self.convert_to_datetime(float(aa.get('start')), 0)
                end_time = \
                    self.convert_to_datetime(float(aa.get('end')), 0)
                aa_output += f"Start Time: {start_time}\n"
                aa_output += f"End Time: {end_time}\n"
                aa_output += f"Alert Description: {aa.get('description')}\n"

                self.layout['alerts'].update(Panel(aa_output))
                self.layout['alerts'].split_row(self.layout)

            self.layout['alerts'].visible = True
            print(self.layout)
        else:
            print("No alerts for this area")


if __name__ == "__main__":
    WeatherAppMain.main()
