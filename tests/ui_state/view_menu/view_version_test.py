"""
The file to test the View Version class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu
from src.ui_state.ui_state import UIState
from src.ui_state.view_menu.view_version import ViewVersion
from src.version import VERSION


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch.object(LiquidCrystal, "print")
def test_view_version(print_mock):
    """
    The function to test ViewVersion's loop function
    """
    state = ViewVersion(Titrator(), MainMenu(Titrator()))
    state.loop()

    assert state.titrator.get_version() == VERSION
    print_mock.assert_any_call("Software Version", line=1)
    print_mock.assert_any_call(VERSION, line=2)


def test_handle_key_4():
    """
    The function to test the back handle key
    """
    titrator = Titrator()

    titrator.state = ViewVersion(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("4")
    assert isinstance(titrator.state, MockPreviousState)


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()

    titrator.state = ViewVersion(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MockPreviousState)
