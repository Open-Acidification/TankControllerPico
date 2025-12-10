"""
The file to test the SetKD class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_kd import SetKD


@mock.patch.object(LiquidCrystal, "print")
def test_set_kd_valid_input(print_mock):
    """
    Unittest that entering a valid KD value sets EEPROM and shows confirmation.
    """
    titrator = Titrator()
    titrator.eeprom.set_kd(50.5)

    state = SetKD(titrator, MainMenu(titrator))
    assert state.value == "50.5"
    state.value = float(state.value)
    state.save_value()

    assert titrator.eeprom.get_kd(36.0) == 50.5
    print_mock.assert_any_call("New KD=50.5", line=2)

    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_user_value_kd_input(print_mock):
    """
    Test entering a KD value through the UserValue interface.
    """
    titrator = Titrator()
    state = SetKD(titrator, MainMenu(titrator))

    state.handle_key("C")
    assert state.value == ""
    state.handle_key("1")
    assert state.value == "1"
    state.handle_key("*")
    assert state.value == "1."
    state.handle_key("9")
    assert state.value == "1.9"
    state.handle_key("A")

    assert titrator.eeprom.get_kd(36.0) == 1.9
    print_mock.assert_any_call("New KD=1.9", line=2)

    assert isinstance(titrator.state.next_state, MainMenu)


def test_set_kd_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = SetKD(titrator, MainMenu(titrator))

    assert state.get_label() == "Set KD"


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()
    titrator.state = SetKD(titrator, MainMenu(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MainMenu)
