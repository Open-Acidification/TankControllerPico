"""
The file to test the View PID Constants class
"""

from unittest import mock

from titration.devices.library import LiquidCrystal
from titration.titrator import Titrator
from titration.ui_state.controller.view_pid_constants import ViewPIDConstants
from titration.ui_state.main_menu import MainMenu
from titration.ui_state.ui_state import UIState


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch.object(LiquidCrystal, "print")
def test_view_pid_constants_show_kp_ki(print_mock):
    """
    The function to test ViewPIDConstants's loop function
    """
    state = ViewPIDConstants(Titrator(), MainMenu(Titrator()))

    state.titrator.pid.kp_value = 1.1
    state.titrator.pid.ki_value = 2.2

    state._start_time = 0.0
    with mock.patch(
        "titration.ui_state.controller.view_pid_constants.time.monotonic",
        return_value=1.0,
    ):
        state.loop()

    print_mock.assert_any_call("Kp: 1.1", line=1)
    print_mock.assert_any_call("Ki: 2.2", line=2)


@mock.patch.object(LiquidCrystal, "print")
def test_view_pid_constants_shows_kd_and_pid_state(print_mock):
    """
    When the loop is in the second phase (elapsed -> 1) it should print Kd on line1 and PID: ON/OFF on line2.
    """
    state = ViewPIDConstants(Titrator(), MainMenu(Titrator()))

    state.titrator.pid.kd_value = 3.3
    state.titrator.ph_control.use_pid = True

    state._start_time = 0.0
    with mock.patch(
        "titration.ui_state.controller.view_pid_constants.time.monotonic",
        return_value=4.0,
    ):
        state.loop()

    print_mock.assert_any_call("Kd: 3.3", line=1)
    print_mock.assert_any_call("PID: ON", line=2)


def test_handle_key_4():
    """
    The function to test the back handle key
    """
    titrator = Titrator()

    titrator.state = ViewPIDConstants(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("4")
    assert isinstance(titrator.state, MockPreviousState)


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()

    titrator.state = ViewPIDConstants(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MockPreviousState)
