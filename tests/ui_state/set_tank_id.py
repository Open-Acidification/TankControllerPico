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
    Unittest that entering a valid tank ID sets EEPROM and shows confirmation.
    """
    titrator = Titrator()
    titrator.eeprom.set_tank_id(5)
    state = SetTankID(titrator, MainMenu(titrator))
    assert state.value == "5"

    state.save_value()
    assert titrator.eeprom.get_tank_id(1) == 5
    print_mock.assert_any_call("New Tank ID=5", line=2)

    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_user_tank_id_string_input(print_mock):
    """
    Test entering a tank ID value through the UserValue interface.
    """
    titrator = Titrator()
    state = SetTankID(titrator, MainMenu(titrator))

    state.handle_key("C")
    assert state.value == ""
    state.handle_key("8")
    assert state.value == "8"
    state.handle_key("3")
    assert state.value == "83"
    state.handle_key("A")

    assert titrator.eeprom.get_tank_id(1) == 83
    print_mock.assert_any_call("New Tank ID=83", line=2)

    assert isinstance(titrator.state.next_state, MainMenu)


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

    assert isinstance(titrator.state.next_state, MainMenu)


def test_set_tank_id_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = SetTankID(titrator, MainMenu(titrator))

    assert state.get_label() == "Set Tank ID#"


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()
    titrator.state = SetTankID(titrator, MainMenu(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MainMenu)
