"""
The file to test the PHCalibration class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_ph_calibration import PHCalibration
from src.ui_state.ui_state import UIState
from src.ui_state.wait import Wait


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch.object(LiquidCrystal, "print")
def test_one_point_calibration(print_mock):
    """
    Test that entering '1' triggers 1-point calibration and returns to main menu.
    """
    titrator = Titrator()
    state = PHCalibration(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("pH Cali: ", line=1)
    print_mock.assert_any_call("1,2 or 3 point?", line=2)

    state.handle_key("1")
    print_mock.assert_any_call("1-pt pH calib...", line=2)

    assert isinstance(titrator.state, Wait)
    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_two_point_calibration(print_mock):
    """
    Test that entering '2' triggers 2-point calibration and returns to main menu.
    """
    titrator = Titrator()
    state = PHCalibration(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("pH Cali: ", line=1)
    print_mock.assert_any_call("1,2 or 3 point?", line=2)

    state.handle_key("2")
    print_mock.assert_any_call("2 Point Cali", line=2)

    assert isinstance(titrator.state, Wait)
    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_three_point_calibration(print_mock):
    """
    Test that entering '3' triggers 3-point calibration and returns to main menu.
    """
    titrator = Titrator()
    state = PHCalibration(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("pH Cali: ", line=1)
    print_mock.assert_any_call("1,2 or 3 point?", line=2)

    state.handle_key("3")
    print_mock.assert_any_call("3 Point Cali", line=2)

    assert isinstance(titrator.state, Wait)
    assert isinstance(titrator.state.next_state, MainMenu)


def test_handle_key_4():
    """
    Test that entering '4' returns to the previous state.
    """
    titrator = Titrator()
    state = PHCalibration(titrator, MockPreviousState(titrator))

    state.handle_key("4")
    assert isinstance(titrator.state, MockPreviousState)


def test_handle_key_d():
    """
    Test that entering 'D' returns to the main menu.
    """
    titrator = Titrator()
    state = PHCalibration(titrator, MockPreviousState(titrator))

    state.handle_key("D")
    assert isinstance(titrator.state, MainMenu)
