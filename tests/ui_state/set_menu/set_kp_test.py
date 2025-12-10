"""
The file to test the SetKP class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_kp import SetKP


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

    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_user_value_kp_input(print_mock):
    """
    Test entering a KP value through the UserValue interface.
    """
    titrator = Titrator()
    state = SetKP(titrator, MainMenu(titrator))

    state.handle_key("C")
    assert state.value == ""
    state.handle_key("2")
    assert state.value == "2"
    state.handle_key("*")
    assert state.value == "2."
    state.handle_key("7")
    assert state.value == "2.7"
    state.handle_key("A")

    assert titrator.eeprom.get_kp(28.0) == 2.7
    print_mock.assert_any_call("New KP=2.7", line=2)

    assert isinstance(titrator.state.next_state, MainMenu)


def test_set_kp_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = SetKP(titrator, MainMenu(titrator))

    assert state.get_label() == "Set KP"


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()
    titrator.state = SetKP(titrator, MainMenu(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MainMenu)
