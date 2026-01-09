"""
The file to test the ResetPHCalibration class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_thermal_calibration_clear import (
    ResetThermalCalibration,
)


@mock.patch.object(LiquidCrystal, "print")
def test_reset_ph_calibration(print_mock):
    """
    Test that pressing 'A' clears pH calibration and transitions to ViewPHCalibration.
    """
    titrator = Titrator()
    state = ResetThermalCalibration(titrator, MainMenu(titrator))
    titrator.thermal_probe.clear_thermal_correction = mock.Mock()

    state.loop()
    print_mock.assert_any_call("A: Clear TempCal", line=1)

    state.handle_key("A")
    titrator.thermal_probe.clear_thermal_correction.assert_called_once()
    print_mock.assert_any_call("Cleared TempCali", line=1)

    assert isinstance(titrator.state.next_state, MainMenu)


def test_set_calibration_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = ResetThermalCalibration(titrator, MainMenu(titrator))

    assert state.get_label() == "A: Clear TempCal"


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()
    titrator.state = ResetThermalCalibration(titrator, MainMenu(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MainMenu)
