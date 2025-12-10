"""
The file to test the View Google Minutes class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.ui_state import UIState
from src.ui_state.view_menu.view_thermal_correction import (
    ViewThermalCorrection,
)


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch.object(LiquidCrystal, "print")
def test_view_thermal_correction(print_mock):
    """
    The function to test ViewThermalCorrection's loop function
    """
    state = ViewThermalCorrection(Titrator(), MainMenu(Titrator()))

    state.loop()

    print_mock.assert_any_call("Temp Cal Offset:", line=1)
    print_mock.assert_any_call("12.0", line=2)


def test_handle_key_4():
    """
    The function to test the back handle key
    """
    titrator = Titrator()

    titrator.state = ViewThermalCorrection(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("4")
    assert isinstance(titrator.state, MockPreviousState)


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()

    titrator.state = ViewThermalCorrection(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MockPreviousState)
