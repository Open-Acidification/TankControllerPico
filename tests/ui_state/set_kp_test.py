"""
The file to test the SetKP class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.controller.set_kp import SetKP
from src.ui_state.main_menu import MainMenu


@mock.patch.object(LiquidCrystal, "print")
def test_set_kp_valid_input(print_mock):
    """
    Test that entering a valid KP value sets EEPROM and shows confirmation.
    """
    titrator = Titrator()
    titrator.eeprom.set_kp(15.5)

    state = SetKP(titrator, MainMenu(titrator))
    assert state.value == "15.5"
    state.value = float(state.value)
    state.save_value()

    assert titrator.eeprom.get_kp(28.0) == 15.5
    print_mock.assert_any_call("New KP=15.5", line=2)

    assert titrator.state.next_state.__class__.__name__ == "MainMenu"


def test_set_kp_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = SetKP(titrator, MainMenu(titrator))

    assert state.get_label() == "Set KP"
