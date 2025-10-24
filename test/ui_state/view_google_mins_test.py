"""
The file to test the View Google Minutes class
"""
from unittest import mock

from titration.devices.library import LiquidCrystal
from titration.titrator import Titrator
from titration.ui_state.main_menu import MainMenu
from titration.ui_state.controller.view_google_mins import ViewGoogleMins


@mock.patch.object(LiquidCrystal, "print")
def test_view_google_mins(print_mock):
    """
    The function to test ViewGoogleMins's loop function
    """
    state = ViewGoogleMins(Titrator(), MainMenu(Titrator()))

    state.loop()

    print_mock.assert_any_call("Google Mins:", line=1)
    print_mock.assert_any_call("108 mins", line=2)


@mock.patch.object(LiquidCrystal, "print")
@mock.patch.object(ViewGoogleMins, "_set_next_state")
def test_handle_key(set_next_state_mock, print_mock):
    """
    The function to test the back and reset handle keys
    """
    main = Titrator().state
    main.handle_key("6")

    state = ViewGoogleMins(Titrator(), previous_state=main)
    state.handle_key("4")

    set_next_state_mock.assert_called()
    prev_state = set_next_state_mock.call_args.args[0]

    prev_state.loop()
    print_mock.assert_any_call("View settings", line=1)
    print_mock.assert_any_call("<4   ^2  8v   6>", line=2)
