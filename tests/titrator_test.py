"""
The file to test the Titrator class
"""

from unittest import mock

from src.devices.library import Keypad
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu


@mock.patch.object(Titrator, "handle_ui")
def test_loop(handle_ui_mock):
    """
    The function to test function calls of the loop function
    """
    titrator = Titrator()

    titrator.loop()
    handle_ui_mock.assert_called()


@mock.patch.object(Titrator, "update_state")
def test_set_next_state_true(update_state_mock):
    """
    The function to test the set_next_state function with update parameter set to True
    """
    titrator = Titrator()

    temp = MainMenu(titrator)
    assert titrator.next_state is None
    titrator.set_next_state(temp, True)
    assert titrator.next_state == temp
    update_state_mock.assert_called()


@mock.patch.object(Titrator, "update_state")
def test_set_next_state_false(update_state_mock):
    """
    The function to test the set_next_state function with update parameter set to False
    """
    titrator = Titrator()

    temp = MainMenu(titrator)
    assert titrator.next_state is None
    titrator.set_next_state(temp, False)
    assert titrator.next_state == temp
    update_state_mock.assert_not_called()


@mock.patch.object(Keypad, "get_key")
@mock.patch.object(MainMenu, "handle_key")
@mock.patch.object(MainMenu, "loop")
def test_handle_ui(keypad_poll_mock, handle_key_mock, loop_mock):
    """
    The function to test function calls of the handle_ui function
    """
    titrator = Titrator()

    titrator.handle_ui()
    keypad_poll_mock.assert_called()
    handle_key_mock.assert_called()
    loop_mock.assert_called()
