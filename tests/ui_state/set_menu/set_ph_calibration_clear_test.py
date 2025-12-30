"""
The file to test the ResetPHCalibration class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_ph_calibration_clear import ResetPHCalibration
from src.ui_state.view_menu.view_ph_calibration import ViewPHCalibration


@mock.patch.object(LiquidCrystal, "print")
def test_reset_ph_calibration(print_mock):
    """
    Test that pressing 'A' clears pH calibration and transitions to ViewPHCalibration.
    """
    titrator = Titrator()
    titrator.ph_probe.clear_calibration = mock.Mock()
    state = ResetPHCalibration(titrator)

    state.loop()
    print_mock.assert_any_call("A: Clear pH Cali", line=1)

    state.handle_key("A")
    titrator.ph_probe.clear_calibration.assert_called_once()
    assert isinstance(titrator.state, ViewPHCalibration)


def test_set_calibration_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = ResetPHCalibration(titrator, MainMenu(titrator))

    assert state.get_label() == "A: Clear pH Cali"


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()
    titrator.state = ResetPHCalibration(titrator, MainMenu(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MainMenu)
