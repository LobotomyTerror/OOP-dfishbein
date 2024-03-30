from textual import on
from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Static, Footer, Header, Log, Label
from textual.widget import Widget
from textual_autocomplete import AutoComplete, Dropdown, DropdownItem
from main import WeatherMain


class LocationSearch(Static):
    # rand = reactive(False, recompose=True)
    def compose(self) -> ComposeResult:
        yield AutoComplete(
            Input('Type Something'),
            Dropdown(items=[
                DropdownItem("Glasgow"),
                DropdownItem("Edinburgh"),
                DropdownItem("Aberdeen"),
                DropdownItem("Dundee"),
            ])
        )


class LocationDetails(Static):
    location = reactive(tuple(), recompose=True)

    def compose(self) -> ComposeResult:
        if self.location:
            yield Label(f"Location being used: {self.location}")


class Location(Static):
    _user_loc = reactive(WeatherMain)
    button = reactive(False, init=False)

    def compose(self) -> ComposeResult:
        yield Button('Yes', variant='success', id='yes', disabled=self.button)
        yield Button('No', variant='error', id='no', disabled=self.button)
        yield LocationDetails('', id='loc')
        yield LocationSearch()
        # yield Log()

    @on(Button.Pressed, '#yes')
    def share_location(self) -> None:
        self._user_loc.find_user_loc()
        self.button = True

    @on(Button.Pressed, '#no')
    def default_location(self) -> None:
        self._user_loc.default_loc()
        self.button = True

    def watch_button(self, button: bool) -> ComposeResult:
        # self.query_one(Log).write_line(f"{button}")
        self.query_one("#yes", Button).disabled = button
        self.query_one("#no", Button).disabled = button
        self.query_one(
            LocationDetails
            ).location = self._user_loc.user_location
        # self.query_one(LocationSearch).disabled = False
        # self.query_one(LocationSearch).rand = True


class WeatherApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Location()


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
