"""
The file to test the SetGoogleSheetInterval class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.controller.set_google_mins import SetGoogleSheetInterval
from src.ui_state.main_menu import MainMenu


@mock.patch.object(LiquidCrystal, "print")
def test_set_google_sheet_interval_valid_input(print_mock):
    """
    Test that entering a valid interval sets EEPROM and shows confirmation.
    """
    titrator = Titrator()
    titrator.eeprom.set_google_sheet_interval(60)
    state = SetGoogleSheetInterval(titrator, MainMenu(titrator))
    assert state.value == "60"

    state.save_value()
    assert titrator.eeprom.get_google_sheet_interval(20) == 60
    print_mock.assert_any_call("New interval=60", line=2)

    assert titrator.state.next_state.__class__.__name__ == "MainMenu"


@mock.patch.object(LiquidCrystal, "print")
def test_set_google_sheet_interval_float_truncates(print_mock):
    """
    Test that float values are truncated to int.
    """
    titrator = Titrator()
    state = SetGoogleSheetInterval(titrator, MainMenu(titrator))
    state.value = 30.7

    state.save_value()

    assert titrator.eeprom.get_google_sheet_interval(20) == 30
    print_mock.assert_any_call("New interval=30", line=2)

    assert titrator.state.next_state.__class__.__name__ == "MainMenu"


def test_set_google_sheet_interval_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = SetGoogleSheetInterval(titrator, MainMenu(titrator))

    assert state.get_label() == "G Sheet Minutes"
