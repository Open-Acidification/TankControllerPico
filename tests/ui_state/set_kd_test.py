"""
The file to test the SetKD class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.controller.set_kd import SetKD
from src.ui_state.main_menu import MainMenu


@mock.patch.object(LiquidCrystal, "print")
def test_set_kd_valid_input(print_mock):
    """
    Test that entering a valid KD value sets EEPROM and shows confirmation.
    """
    titrator = Titrator()
    titrator.eeprom.set_kd(50.5)

    state = SetKD(titrator, MainMenu(titrator))
    assert state.value == "50.5"
    state.value = float(state.value)
    state.save_value()

    assert titrator.eeprom.get_kd(36.0) == 50.5
    print_mock.assert_any_call("New KD=50.5", line=2)


def test_set_kd_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = SetKD(titrator, MainMenu(titrator))

    assert state.get_label() == "Set KD"
