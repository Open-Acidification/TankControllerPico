"""
The file to test the SetThermalCalibration class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_thermal_calibration import SetThermalCalibration


@mock.patch.object(LiquidCrystal, "print")
def test_set_thermal_calibration_valid_input(print_mock):
    """
    Unittest that entering a valid tank ID sets EEPROM and shows confirmation.
    """
    titrator = Titrator()
    titrator.thermal_probe.set_thermal_correction(2.5)
    state = SetThermalCalibration(titrator, MainMenu(titrator))
    assert state.value == "2.5"

    state.save_value()
    assert titrator.thermal_probe.get_thermal_correction() == 2.5
    print_mock.assert_any_call("New correction=2.5", line=2)

    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_user_thermal_calibration_string_input(print_mock):
    """
    Test entering a tank ID value through the UserValue interface.
    """
    titrator = Titrator()
    state = SetThermalCalibration(titrator, MainMenu(titrator))

    state.handle_key("C")
    assert state.value == ""
    state.handle_key("1")
    assert state.value == "1"
    state.handle_key("0")
    assert state.value == "10"
    state.handle_key("A")

    assert titrator.thermal_probe.get_thermal_correction() == 10
    print_mock.assert_any_call("New correction=10.0", line=2)

    assert isinstance(titrator.state.next_state, MainMenu)


def test_set_thermal_calibration_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = SetThermalCalibration(titrator, MainMenu(titrator))

    assert state.get_label() == "Real Temperature"


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()
    titrator.state = SetThermalCalibration(titrator, MainMenu(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MainMenu)
