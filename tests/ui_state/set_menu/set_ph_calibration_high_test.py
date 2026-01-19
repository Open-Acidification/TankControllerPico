"""
The file to test the PHCalibrationHigh class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.set_menu.set_ph_calibration_high import PHCalibrationHigh
from src.ui_state.set_menu.set_ph_calibration_low import PHCalibrationLow
from src.ui_state.ui_state import UIState


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch.object(LiquidCrystal, "print")
def test_ph_calibration_high(print_mock):
    """
    Test the PHCalibrationHigh state.
    """
    titrator = Titrator()
    state = PHCalibrationHigh(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("High buffer pH", line=1)

    state.value = "10.0"
    state.save_value()
    assert titrator.ph_probe._highpoint_calibration == 10.0
    print_mock.assert_any_call("High = 10.0", line=2)

    assert isinstance(titrator.state, PHCalibrationLow)
    assert isinstance(titrator.state.previous_state, PHCalibrationHigh)
