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


@mock.patch.object(LiquidCrystal, "print")
def test_view_time_loop_prints_datetime_and_uptime(print_mock):
    """
    The function to test ViewTime's loop function
    """
    state = ViewTime(Titrator(), MainMenu(Titrator()))
    fixed_now = datetime(2025, 11, 14, 9, 42)
    fixed_start = fixed_now - timedelta(days=1, hours=2, minutes=3, seconds=4)
    state._start_time = fixed_start

    with mock.patch("titration.ui_state.controller.view_time.datetime") as mock_dt:
        mock_dt.now.return_value = fixed_now
        state.loop()
    print_mock.assert_any_call(
        f"{fixed_now.year:04d}-{fixed_now.month:02d}-{fixed_now.day:02d} {fixed_now.hour:02d}:{fixed_now.minute:02d}",
        line=1,
    )

    elapsed = fixed_now - fixed_start
    days = elapsed.days
    hours, rem = divmod(elapsed.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    print_mock.assert_any_call(
        f"Up d:{days:02d} {hours:02d}:{minutes:02d}:{seconds:02d}", line=2
    )


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
