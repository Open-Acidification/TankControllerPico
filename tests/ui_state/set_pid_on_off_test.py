"""
The file to test the EnablePID class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.controller.set_pid_on_off import EnablePID
from src.ui_state.main_menu import MainMenu
from src.ui_state.ui_state import UIState
from src.ui_state.wait import Wait


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch.object(LiquidCrystal, "print")
def test_enable_pid_input(print_mock):
    """
    Test that entering '1' enables PID and shows confirmation.
    """
    titrator = Titrator()
    state = EnablePID(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("PID 1:on; 9:off", line=1)

    state.handle_key("1")
    assert titrator.ph_control.use_pid is True
    print_mock.assert_any_call("PID enabled", line=2)

    assert isinstance(titrator.state, Wait)
    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_disable_pid_input(print_mock):
    """
    Test that entering '9' enables PID and shows confirmation.
    """
    titrator = Titrator()
    state = EnablePID(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("PID 1:on; 9:off", line=1)

    state.handle_key("9")
    assert titrator.ph_control.use_pid is False
    print_mock.assert_any_call("PID disabled", line=2)

    assert isinstance(titrator.state, Wait)
    assert isinstance(titrator.state.next_state, MainMenu)


@mock.patch.object(LiquidCrystal, "print")
def test_handle_key_a(print_mock):
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()
    state = EnablePID(titrator, MockPreviousState(titrator))

    state.loop()
    print_mock.assert_any_call("PID 1:on; 9:off", line=1)
    print_mock.assert_any_call("Currently enabled", line=2)

    state.handle_key("A")
    assert titrator.ph_control.use_pid is True
    print_mock.assert_any_call("PID enabled", line=2)

    assert isinstance(titrator.state, Wait)
    assert isinstance(titrator.state.next_state, MainMenu)

def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()
    titrator.state = EnablePID(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MockPreviousState)
