"""
The file to test the View PH Calibration class
"""

from unittest import mock

from titration.devices.library import LiquidCrystal
from titration.titrator import Titrator
from titration.ui_state.controller.view_ph_calibration import ViewPHCalibration
from titration.ui_state.main_menu import MainMenu
from titration.ui_state.ui_state import UIState


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch.object(LiquidCrystal, "print")
def test_view_ph_calibration(print_mock):
    """
    The function to test ViewGoogleSheetInterval's loop function
    """
    mock_probe = mock.Mock()
    mock_probe.send_calibration_request = mock.Mock()
    mock_probe.send_slope_request = mock.Mock()
    mock_probe.get_calibration.return_value = "PH Calibration"
    mock_probe.get_slope.return_value = "99.7,100.3,-0.89"

    with mock.patch("titration.ui_state.controller.view_ph_calibration.PHProbe", return_value=mock_probe):
        state = ViewPHCalibration(Titrator(), MainMenu(Titrator()))
        state.loop()

    mock_probe.send_calibration_request.assert_called_once()
    mock_probe.send_slope_request.assert_called_once()
    print_mock.assert_any_call("PH Calibration", line=1)
    print_mock.assert_any_call("99.7,100.3,-0.89", line=2)


def test_handle_key_4():
    """
    The function to test the back handle key
    """
    titrator = Titrator()

    titrator.state = ViewPHCalibration(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("4")
    assert isinstance(titrator.state, MockPreviousState)


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()

    titrator.state = ViewPHCalibration(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MockPreviousState)
