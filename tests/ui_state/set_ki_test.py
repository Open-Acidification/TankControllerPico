"""
The file to test the SetKI class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.controller.set_ki import SetKI
from src.ui_state.main_menu import MainMenu


@mock.patch.object(LiquidCrystal, "print")
def test_set_ki_valid_input(print_mock):
    """
    Test that entering a valid KI value sets EEPROM and shows confirmation.
    """
    titrator = Titrator()
    titrator.eeprom.set_ki(2.5)

    state = SetKI(titrator, MainMenu(titrator))
    assert state.value == "2.5"
    state.value = float(state.value)
    state.save_value()

    assert titrator.eeprom.get_ki(28.0) == 2.5
    print_mock.assert_any_call("New KI=2.5", line=2)

    assert titrator.state.next_state.__class__.__name__ == "MainMenu"


def test_set_ki_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = SetKI(titrator, MainMenu(titrator))

    assert state.get_label() == "Set KI"
