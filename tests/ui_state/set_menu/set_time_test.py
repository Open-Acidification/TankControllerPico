"""
Test suite for the SetTime class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_time import SetTime


@mock.patch.object(LiquidCrystal, "print")
def test_set_time_handle_key(print_mock):
    """
    Test that handle_key processes key presses correctly.
    """
    titrator = Titrator()
    state = SetTime(titrator, MainMenu(titrator))

    state.handle_key("2")
    state.handle_key("0")
    state.handle_key("2")
    state.handle_key("5")
    state.handle_key("A")

    state.loop()
    assert state.sub_state == 1
    assert state.values[0] == "2025"
    print_mock.assert_any_call("Month (1-12):", line=1)
    print_mock.assert_any_call("", style="center", line=2)


def test_set_time_advances_substates():
    """
    Test that the state advances through substates correctly.
    """
    titrator = Titrator()
    state = SetTime(titrator, MainMenu(titrator))

    state.value = "2025"
    state.save_value()
    assert state.sub_state == 1
    state.value = "12"
    state.save_value()
    assert state.sub_state == 2
    state.value = "10"
    state.save_value()
    assert state.sub_state == 3
    state.value = "15"
    state.save_value()
    assert state.sub_state == 4
    state.value = "30"
    state.save_value()
    assert state.sub_state == 5


@mock.patch.object(LiquidCrystal, "print")
def test_set_time_valid_input(mock_print):
    """
    Test that valid date/time inputs are saved and displayed correctly.
    """
    titrator = Titrator()
    state = SetTime(titrator, MainMenu(titrator))

    state.value = "2025"
    state.save_value()
    state.value = "12"
    state.save_value()
    state.value = "10"
    state.save_value()
    state.value = "15"
    state.save_value()
    state.value = "30"
    state.save_value()

    mock_print.assert_any_call("New Date/Time:", line=1)
    mock_print.assert_any_call("2025-12-10 15:30", line=2)
    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_set_time_invalid_month(mock_print):
    """
    Test that an invalid month input is handled gracefully.
    """
    titrator = Titrator()
    state = SetTime(titrator, MainMenu(titrator))

    state.value = "2025"
    state.save_value()
    state.value = "99"  # Invalid month
    state.save_value()
    state.value = "10"
    state.save_value()
    state.value = "15"
    state.save_value()
    state.value = "30"
    state.save_value()

    mock_print.assert_any_call("Invalid Date/Time", line=1)
    mock_print.assert_any_call("month must be in 1..12, not 99", line=2)
    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_set_time_invalid_day(mock_print):
    """
    Test that an invalid day input is handled gracefully.
    """
    titrator = Titrator()
    state = SetTime(titrator, MainMenu(titrator))

    state.value = "2025"
    state.save_value()
    state.value = "12"
    state.save_value()
    state.value = "32"  # Invalid day
    state.save_value()
    state.value = "15"
    state.save_value()
    state.value = "30"
    state.save_value()

    mock_print.assert_any_call("Invalid Date/Time", line=1)
    mock_print.assert_any_call(
        "day 32 must be in range 1..31 for month 12 in year 2025", line=2
    )
    assert isinstance(titrator.state.next_state, MainMenu)
