"""
The file to test the SetChillOrHeat class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.set_menu.set_chill_or_heat import SetChillOrHeat
from src.ui_state.ui_state import UIState
from src.ui_state.wait import Wait


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch.object(LiquidCrystal, "print")
def test_set_heat(print_mock):
    """
    Test that entering '9' sets to Heat and shows confirmation."""
    titrator = Titrator()
    state = SetChillOrHeat(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("1:Chill; 9:Heat", line=1)

    state.handle_key("9")
    assert titrator.thermal_control.get_heat(False) is True
    print_mock.assert_any_call("Use heater", line=2)

    assert isinstance(titrator.state, Wait)
    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_set_chill(print_mock):
    """
    Test that entering '1' sets to Chill and shows confirmation.
    """
    titrator = Titrator()
    state = SetChillOrHeat(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("1:Chill; 9:Heat", line=1)

    state.handle_key("1")
    assert titrator.thermal_control.get_heat(True) is False
    print_mock.assert_any_call("Use chiller", line=2)

    assert isinstance(titrator.state, Wait)
    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_handle_key_a(print_mock):
    """
    Test that entering 'A' shows current setting and returns to main menu.
    """
    titrator = Titrator()
    state = SetChillOrHeat(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("1:Chill; 9:Heat", line=1)
    print_mock.assert_any_call("Currently: Heat", line=2)

    state.handle_key("A")
    print_mock.assert_any_call("Use heater", line=2)
    assert titrator.thermal_control.get_heat(True) is True

    assert isinstance(titrator.state, Wait)
    assert isinstance(titrator.state.next_state, MainMenu)


def test_handle_key_d():
    """
    Test that entering 'D' returns to the previous state.
    """
    titrator = Titrator()
    state = SetChillOrHeat(titrator, MockPreviousState(titrator))

    state.handle_key("D")
    assert isinstance(titrator.state, MockPreviousState)
