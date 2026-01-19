"""
Test suite for the SetThermalTarget class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_thermal_target import SetThermalTarget


@mock.patch.object(LiquidCrystal, "print")
def test_set_thermal_target_handle_key(print_mock):
    """
    Test that handle_key processes key presses correctly.
    """
    titrator = Titrator()
    state = SetThermalTarget(titrator, MainMenu(titrator))

    state.loop()
    print_mock.assert_any_call("Set Temperature", line=1)

    state.handle_key("7")
    state.handle_key("A")
    assert state.sub_state == 1
    assert state.values[0] == 7

    state.loop()
    print_mock.assert_any_call("Set ramp hours:", line=1)
    print_mock.assert_any_call("", style="center", line=2)


def test_set_thermal_target_advances_substates():
    """
    Test that the state advances through substates correctly.
    """
    titrator = Titrator()
    state = SetThermalTarget(titrator, MainMenu(titrator))

    state.value = "7.5"
    state.save_value()
    assert state.sub_state == 1
    state.value = "2"
    state.save_value()
    assert state.sub_state == 2


@mock.patch.object(LiquidCrystal, "print")
def test_set_ph_target_valid_input(print_mock):
    """
    Test that valid pH target and ramp inputs are saved and displayed correctly.
    """
    titrator = Titrator()
    titrator.thermal_control = mock.Mock()
    state = SetThermalTarget(titrator, MainMenu(titrator))

    state.value = "7.5"
    state.save_value()
    state.value = "2"
    state.save_value()

    titrator.thermal_control.set_base_thermal_target.assert_called_once_with(7.5)
    titrator.thermal_control.set_ramp_duration_hours.assert_called_once_with(2.0)

    print_mock.assert_any_call("New Temp=7.50", line=1)
    print_mock.assert_any_call("New Ramp=2.00", line=2)
    assert isinstance(titrator.state.next_state, MainMenu)


def test_set_thermal_target_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = SetThermalTarget(titrator, MainMenu(titrator))

    assert state.get_label() == "Set Temperature"
    state.sub_state = 1
    assert state.get_label() == "Set ramp hours:"


def test_handle_key_d():
    """
    Test that entering 'D' returns to the main menu.
    """
    titrator = Titrator()
    state = SetThermalTarget(titrator, MainMenu(titrator))

    state.handle_key("D")
    assert isinstance(titrator.state, MainMenu)
