"""
The file to test the ViewPH class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.ui_state import UIState
from src.ui_state.view_menu.view_ph import ViewPH


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


@mock.patch.object(LiquidCrystal, "print")
def test_view_ph_shows_header_and_values(print_mock):
    """
    Test that the ViewPH class displays the header and pH values in the first phase of the loop.
    """
    titrator = Titrator()
    titrator.ph_probe.get_ph_value = mock.Mock(return_value=7.5)
    titrator.ph_control.get_current_target_ph = mock.Mock(return_value=8.0)
    titrator.ph_control.get_base_target_ph = mock.Mock(return_value=8.5)

    state = ViewPH(titrator, MockPreviousState(titrator))
    state._start_time = 0.0
    with mock.patch(
        "src.ui_state.view_menu.view_ph.time.monotonic",
        return_value=1.0,
    ):
        state.loop()

    print_mock.assert_any_call("Now  Next  Goal", 1)
    print_mock.assert_any_call("7.50 8.000 8.500", 2)


@mock.patch.object(LiquidCrystal, "print")
def test_view_ph_shows_function_flat_type(print_mock):
    """
    Test that the ViewPH class displays the pH function type and no variables for FLAT_TYPE.
    """
    titrator = Titrator()
    titrator.ph_control.get_ph_function_type = mock.Mock(
        return_value=titrator.ph_control.FLAT_TYPE
    )

    state = ViewPH(titrator, MockPreviousState(titrator))
    state._start_time = 0.0

    with mock.patch("src.ui_state.view_menu.view_ph.time.monotonic", return_value=4.0):
        state.loop()

    print_mock.assert_any_call("type: flat", 1)
    print_mock.assert_any_call("", 2)


@mock.patch.object(LiquidCrystal, "print")
def test_view_ph_shows_function_ramp_type_and_variables(print_mock):
    """
    Test that the ViewPH class displays the pH function type and variables in the second phase of the loop.
    """
    titrator = Titrator()
    titrator.ph_control.get_ph_function_type = mock.Mock(
        return_value=titrator.ph_control.RAMP_TYPE
    )
    titrator.ph_control.get_ramp_time_end = mock.Mock(return_value=4000)

    state = ViewPH(titrator, MockPreviousState(titrator))
    state._start_time = 0.0

    with mock.patch("src.ui_state.view_menu.view_ph.time.monotonic", return_value=4.0):
        state.loop()

    current_time = int(4.0)
    time_left = 4000 - current_time
    time_left_hours = time_left // 3600
    time_left_minutes = (time_left % 3600) // 60
    time_left_seconds = time_left % 60
    expected_message = (
        f"left: {time_left_hours}:{time_left_minutes}:{time_left_seconds}"
    )

    print_mock.assert_any_call("type: ramp", 1)
    print_mock.assert_any_call(expected_message, 2)


@mock.patch.object(LiquidCrystal, "print")
def test_view_ph_shows_function_sine_type_and_variables(print_mock):
    """
    Test that the ViewPH class displays the pH function type and variables for SINE_TYPE.
    """
    titrator = Titrator()
    titrator.ph_control.get_ph_function_type = mock.Mock(
        return_value=titrator.ph_control.SINE_TYPE
    )
    titrator.ph_control.get_period_in_seconds = mock.Mock(return_value=7200)  # 2 hours
    titrator.ph_control.get_amplitude = mock.Mock(return_value=0.5)

    state = ViewPH(titrator, MockPreviousState(titrator))
    state._start_time = 0.0

    with mock.patch("src.ui_state.view_menu.view_ph.time.monotonic", return_value=4.0):
        state.loop()

    period_hours = 7200 / 3600.0
    amplitude = 0.5
    expected_message = f"p={period_hours:.3f} a={amplitude:.3f}"

    print_mock.assert_any_call("type: sine", 1)
    print_mock.assert_any_call(expected_message, 2)


def test_handle_key_4():
    """
    Test that pressing key 4 returns to the previous state.
    """
    titrator = Titrator()
    titrator.state = ViewPH(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("4")
    assert isinstance(titrator.state, MockPreviousState)


def test_handle_key_d():
    """
    Test that pressing key D returns to the previous state.
    """
    titrator = Titrator()
    titrator.state = ViewPH(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MockPreviousState)
