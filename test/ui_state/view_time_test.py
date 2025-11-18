"""
The file to test the View Time class
"""

from datetime import datetime, timedelta
from unittest import mock

from titration.devices.library import LiquidCrystal
from titration.titrator import Titrator
from titration.ui_state.controller.view_time import ViewTime
from titration.ui_state.main_menu import MainMenu
from titration.ui_state.ui_state import UIState


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch("titration.ui_state.controller.view_time.datetime")
@mock.patch.object(LiquidCrystal, "print")
def test_view_time_loop_prints_datetime_and_uptime(print_mock, mock_dt):
    """
    The function to test ViewTime's loop function
    """
    state = ViewTime(Titrator(), MainMenu(Titrator()))

    fixed_now = datetime(2025, 11, 14, 9, 42)
    fixed_start = fixed_now - timedelta(days=1, hours=2, minutes=3, seconds=4)
    state._start_time = fixed_start

    mock_dt.now.return_value = fixed_now
    state.loop()

    print_mock.assert_any_call("2025-11-14 09:42", line=1)
    print_mock.assert_any_call(f"Up d:{1:02d} {2:02d}:{3:02d}:{4:02d}", line=2)


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
