"""
The file to test the View Google Minutes class
"""
from unittest import mock

from titration.devices.library import LiquidCrystal
from titration.titrator import Titrator
from titration.ui_state.main_menu import MainMenu   
from titration.ui_state.controller.view_google_sheet_interval import ViewGoogleSheetInterval


@mock.patch.object(LiquidCrystal, "print")
def test_view_google_sheet_interval(print_mock):
    """
    The function to test ViewGoogleSheetInterval's loop function
    """
    state = ViewGoogleSheetInterval(Titrator(), MainMenu(Titrator()))

    state.loop()

    print_mock.assert_any_call("Google Mins:", line=1)
    print_mock.assert_any_call("20", line=2)


def test_handle_key():
    """
    The function to test the back and reset handle keys
    """
    titrator = Titrator()
    main = titrator.state
    main.handle_key("6")
    main.handle_key("6")
    main.handle_key("8")
    main.handle_key("8")

    main.handle_key("6")
    assert isinstance(titrator.state, ViewGoogleSheetInterval)

    titrator.state.handle_key("4")
    assert isinstance(titrator.state, MainMenu)
