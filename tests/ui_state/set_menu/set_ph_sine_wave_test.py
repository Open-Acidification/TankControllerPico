"""
Test suite for the SetPHSineWave class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_ph_sine_wave import SetPHSineWave


@mock.patch.object(LiquidCrystal, "print")
def test_set_ph_sine_wave_handle_key(print_mock):
    """
    Test that handle_key processes key presses correctly.
    """
    titrator = Titrator()
    state = SetPHSineWave(titrator, MainMenu(titrator))

    state.handle_key("7")
    state.handle_key("A")

    assert state.sub_state == 1
    assert state.values[0] == 7

    state.loop()
    print_mock.assert_any_call("Set Amplitude:", line=1)
    print_mock.assert_any_call("", style="center", line=2)


def test_set_ph_sine_wave_advances_substates():
    """
    Test that the state advances through substates correctly.
    """
    titrator = Titrator()
    state = SetPHSineWave(titrator, MainMenu(titrator))

    state.value = "7.5"
    state.save_value()
    assert state.sub_state == 1
    state.value = "2.0"
    state.save_value()
    assert state.sub_state == 2
    state.value = "24.0"
    state.save_value()
    assert state.sub_state == 3


@mock.patch.object(LiquidCrystal, "print")
def test_set_ph_sine_wave_valid_input(print_mock):
    """
    Test that valid pH mean, amplitude, and period inputs are saved and displayed correctly.
    """
    titrator = Titrator()
    titrator.ph_control = mock.Mock()
    state = SetPHSineWave(titrator, MainMenu(titrator))

    state.value = "7.5"
    state.save_value()
    state.value = "2.0"
    state.save_value()
    state.value = "24.0"
    state.save_value()

    titrator.ph_control.set_base_target_ph.assert_called_once_with(7.5)
    titrator.ph_control.set_sine_amplitude_and_hours.assert_called_once_with(2.0, 24.0)

    print_mock.assert_any_call("New pH=7.500", line=1)
    print_mock.assert_any_call("A=2.000 P=24.000", line=2)
    assert isinstance(titrator.state.next_state, MainMenu)


def test_set_ph_sine_wave_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = SetPHSineWave(titrator, MainMenu(titrator))

    assert state.get_label() == "Set pH Mean:"
    state.sub_state = 1
    assert state.get_label() == "Set Amplitude:"
    state.sub_state = 2
    assert state.get_label() == "Set Period hrs:"


def test_handle_key_d():
    """
    Test that entering 'D' returns to the main menu.
    """
    titrator = Titrator()
    state = SetPHSineWave(titrator, MainMenu(titrator))

    state.handle_key("D")
    assert isinstance(titrator.state, MainMenu)
