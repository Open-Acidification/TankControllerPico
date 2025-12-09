"""
The file to test the EnablePID class
"""

from unittest import mock

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.controller.set_pid_on_off import EnablePID
from src.ui_state.main_menu import MainMenu


@mock.patch.object(LiquidCrystal, "print")
def test_enable_pid_valid_input_enable(print_mock):
    """
    Test that entering '1' enables PID and shows confirmation.
    """
    titrator = Titrator()
    state = EnablePID(titrator, MainMenu(titrator))
    state.value = 1.0

    state.save_value()

    assert titrator.ph_control.use_pid is True
    print_mock.assert_any_call("PID enabled", line=1)

    assert titrator.state.next_state.__class__.__name__ == "MainMenu"


@mock.patch.object(LiquidCrystal, "print")
def test_enable_pid_valid_input_disable(print_mock):
    """
    Test that entering '9' disables PID and shows confirmation.
    """
    titrator = Titrator()
    state = EnablePID(titrator, MainMenu(titrator))
    state.value = 9.0

    state.save_value()

    assert titrator.ph_control.use_pid is False
    print_mock.assert_any_call("PID disabled", line=1)

    assert titrator.state.next_state.__class__.__name__ == "MainMenu"


@mock.patch.object(LiquidCrystal, "print")
def test_enable_pid_invalid_input(print_mock):
    """
    Test that invalid input shows error and transitions to wait state.
    """
    titrator = Titrator()
    main_menu = MainMenu(titrator)
    state = EnablePID(titrator, main_menu)
    state.value = 5.0

    state.save_value()

    print_mock.assert_any_call("Invalid entry", line=1)

    assert titrator.state is not state
    assert isinstance(titrator.state.next_state, EnablePID)


def test_enable_pid_get_label():
    """
    Test the label returned by get_label.
    """
    titrator = Titrator()
    state = EnablePID(titrator, MainMenu(titrator))

    assert state.get_label() == "PID 1:on; 9:off"
