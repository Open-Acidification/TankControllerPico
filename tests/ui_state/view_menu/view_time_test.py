"""
The file to test the View Time class
"""

from datetime import datetime, timedelta
from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.ui_state import UIState
from src.ui_state.view_menu.view_time import ViewTime


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch("src.devices.date_time.DateTime.uptime")
@mock.patch("src.devices.date_time.DateTime.current")
@mock.patch.object(LiquidCrystal, "print")
def test_view_time_loop_prints_datetime_and_uptime(print_mock, mock_current, mock_uptime):
    """
    The function to test ViewTime's loop function
    """
    state = ViewTime(Titrator(), MainMenu(Titrator()))

    mock_current.return_value = datetime(2025, 11, 14, 9, 42)
    mock_uptime.return_value = timedelta(days=1, hours=2, minutes=3, seconds=4)
    state.loop()

    print_mock.assert_any_call("2025-11-14 09:42", line=1)
    print_mock.assert_any_call("Up d:01 02:03:04", line=2)


def test_handle_key_4():
    """
    The function to test the back handle key
    """
    titrator = Titrator()

    titrator.state = ViewTime(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("4")
    assert isinstance(titrator.state, MockPreviousState)


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()

    titrator.state = ViewTime(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MockPreviousState)
