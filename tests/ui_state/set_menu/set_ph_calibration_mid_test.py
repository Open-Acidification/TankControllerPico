"""
The file to test the PHCalibrationMid class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_ph_calibration_high import PHCalibrationHigh
from src.ui_state.set_menu.set_ph_calibration_low import PHCalibrationLower
from src.ui_state.set_menu.set_ph_calibration_mid import (
    PHCalibrationHigher,
    PHCalibrationMid,
    PHCalibrationOnly,
)
from src.ui_state.ui_state import UIState


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch.object(LiquidCrystal, "print")
def test_ph_calibration_only(print_mock):
    """
    Test the PHCalibrationOnly state.
    """
    titrator = Titrator()
    state = PHCalibrationOnly(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("Buffer pH", line=1)

    state.value = "7.0"
    state.save_value()
    assert titrator.ph_probe._midpoint_calibration == 7.0
    print_mock.assert_any_call("Buffer = 7.0", line=2)

    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_ph_calibration_higher(print_mock):
    """
    Test the PHCalibrationHigher state.
    """
    titrator = Titrator()
    state = PHCalibrationHigher(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("Higher buffer pH", line=1)

    state.value = "9.0"
    state.save_value()
    assert titrator.ph_probe._midpoint_calibration == 9.0
    print_mock.assert_any_call("Mid = 9.0", line=2)

    assert isinstance(titrator.state, PHCalibrationLower)
    assert isinstance(titrator.state.previous_state, PHCalibrationHigher)


@mock.patch.object(LiquidCrystal, "print")
def test_ph_calibration_mid(print_mock):
    """
    Test the PHCalibrationMid state.
    """
    titrator = Titrator()
    state = PHCalibrationMid(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("Mid buffer pH", line=1)

    state.value = "12.3"
    state.save_value()
    assert titrator.ph_probe._midpoint_calibration == 12.3
    print_mock.assert_any_call("Mid = 12.3", line=2)

    assert isinstance(titrator.state, PHCalibrationHigh)
    assert isinstance(titrator.state.previous_state, PHCalibrationMid)
