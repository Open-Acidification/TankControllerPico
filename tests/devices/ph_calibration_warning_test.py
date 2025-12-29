"""
Unit tests for the PHCalibrationWarning UI state.
"""

from unittest import mock

from src.devices.ph_calibration_warning import PHCalibrationWarning
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.ui_state import UIState
from src.ui_state.view_menu.view_ph_calibration import ViewPHCalibration


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch("src.devices.ph_probe_mock.PHProbe.get_slope", return_value="Slope: 99.7")
@mock.patch("src.devices.library.LiquidCrystal.print")
def test_loop_warning_message(print_mock, _mock_get_slope):
    """
    Test the loop method to ensure the warning message and slope are displayed correctly.
    """
    titrator = Titrator()
    state = PHCalibrationWarning(titrator, MainMenu(titrator))

    # Simulate the loop
    state.loop()

    # Verify the warning message and slope are displayed
    print_mock.assert_any_call("BAD CALIBRATION?", line=1)
    print_mock.assert_any_call("Slope: 99.7", line=2)


def test_handle_key_a():
    """
    Test that pressing 'A' sets ignore_bad_ph_slope to True and returns to the previous state.
    """
    titrator = Titrator()
    state = PHCalibrationWarning(titrator, MockPreviousState(titrator))

    state.handle_key("A")
    assert titrator.ph_probe.eeprom.get_ignore_bad_ph_slope(True) is True

    assert isinstance(titrator.state, MockPreviousState)


def test_handle_key_c():
    """
    Test that pressing 'C' clears the calibration and transitions to ViewPHCalibration state.
    """
    titrator = Titrator()
    state = PHCalibrationWarning(titrator, MockPreviousState(titrator))

    state.handle_key("C")

    assert titrator.ph_probe.get_calibration() == ""
    assert titrator.ph_probe.slope_is_out_of_range is False
    assert titrator.ph_probe.eeprom.get_ignore_bad_ph_slope(True) is False

    assert isinstance(titrator.state, ViewPHCalibration)
