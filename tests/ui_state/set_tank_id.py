"""
The file to test the SetTankID class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.controller.set_tank_id import SetTankID
from src.ui_state.main_menu import MainMenu


@mock.patch.object(LiquidCrystal, "print")
def test_set_tank_id_valid_input(print_mock):
    """
    Test that entering a valid tank ID sets EEPROM and shows confirmation.
    """
    titrator = Titrator()
    titrator.eeprom.set_tank_id(5)
    state = SetTankID(titrator, MainMenu(titrator))
    assert state.value == "5"

    state.save_value()
    assert titrator.eeprom.get_tank_id(1) == 5
    print_mock.assert_any_call("New Tank ID=5", line=2)

    assert titrator.state.next_state.__class__.__name__ == "MainMenu"


@mock.patch.object(LiquidCrystal, "print")
def test_set_tank_id_truncates(print_mock):
    """
    Test that SetTankID initializes with the current EEPROM value.
    """
    titrator = Titrator()
    state = SetTankID(titrator, MainMenu(titrator))
    state.value = 7.9

    state.save_value()

    assert titrator.eeprom.get_tank_id(1) == 7
    print_mock.assert_any_call("New Tank ID=7", line=2)

    assert titrator.state.next_state.__class__.__name__ == "MainMenu"


def test_set_tank_id_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = SetTankID(titrator, MainMenu(titrator))

    assert state.get_label() == "Set Tank ID#"


@mock.patch.object(LiquidCrystal, "print")
def test_set_tank_id_returns_to_main_menu():
    """
    Test that save_value transitions to a Wait state that will go to MainMenu.
    """
    titrator = Titrator()
    state = SetTankID(titrator, MainMenu(titrator))
    state.value = "3"
    state.value = float(state.value)

    state.save_value()

    assert titrator.state is not state
    assert titrator.state.next_state.__class__.__name__ == "MainMenu"
