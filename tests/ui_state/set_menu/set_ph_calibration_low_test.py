"""
The file to test the PHCalibrationLow class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_ph_calibration_low import (
    PHCalibrationLow,
    PHCalibrationLower,
)
from src.ui_state.ui_state import UIState


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch.object(LiquidCrystal, "print")
def test_ph_calibration_lower(print_mock):
    """
    Test the PHCalibrationLower state.
    """
    titrator = Titrator()
    state = PHCalibrationLower(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("Lower buffer pH", line=1)

    state.value = "3.5"
    state.save_value()
    assert titrator.ph_probe._lowpoint_calibration == 3.5
    print_mock.assert_any_call("Low = 3.5", line=2)

    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_ph_calibration_low(print_mock):
    """
    Test the PHCalibrationLow state.
    """
    titrator = Titrator()
    state = PHCalibrationLow(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("Low buffer pH", line=1)

    state.value = "4.0"
    state.save_value()
    assert titrator.ph_probe._lowpoint_calibration == 4.0
    print_mock.assert_any_call("Low = 4.0", line=2)

    assert isinstance(titrator.state.next_state, MainMenu)
