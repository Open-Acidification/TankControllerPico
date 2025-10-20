"""
The file to test the TankController class
"""

from unittest import mock

from tank_controller.devices.library import Keypad
from tank_controller.tank_controller import TankController
from tank_controller.ui_state.main_menu import MainMenu
from tank_controller.ui_state.titration.setup_titration import SetupTitration


@mock.patch.object(TankController, "handle_ui")
def test_loop(handle_ui_mock):
    """
    The function to test function calls of the loop function
    """
    tank_controller = TankController()

    tank_controller.loop()
    handle_ui_mock.assert_called()


@mock.patch.object(TankController, "update_state")
def test_set_next_state_true(update_state_mock):
    """
    The function to test the set_next_state function with update parameter set to True
    """
    tank_controller = TankController()

    temp = MainMenu(tank_controller)
    assert tank_controller.next_state is None
    tank_controller.set_next_state(temp, True)
    assert tank_controller.next_state == temp
    update_state_mock.assert_called()


@mock.patch.object(TankController, "update_state")
def test_set_next_state_false(update_state_mock):
    """
    The function to test the set_next_state function with update parameter set to False
    """
    tank_controller = TankController()

    temp = MainMenu(tank_controller)
    assert tank_controller.next_state is None
    tank_controller.set_next_state(temp, False)
    assert tank_controller.next_state == temp
    update_state_mock.assert_not_called()


@mock.patch.object(SetupTitration, "start")
def test_update_state_without_next_state(start_mock):
    """
    The function to test the start function when the titrator does not have a next_state
    """
    tank_controller = TankController()

    assert tank_controller.next_state is None
    tank_controller.update_state()
    start_mock.assert_not_called()


@mock.patch.object(SetupTitration, "start")
def test_update_state_with_next_state(start_mock):
    """
    The function to test the start function when the titrator has a next_state
    """
    tank_controller = TankController()

    temp = SetupTitration(tank_controller)
    tank_controller.next_state = temp
    assert tank_controller.state != tank_controller.next_state
    tank_controller.update_state()
    assert tank_controller.state == temp
    assert tank_controller.next_state is None
    start_mock.assert_called()


@mock.patch.object(Keypad, "get_key")
@mock.patch.object(MainMenu, "handle_key")
@mock.patch.object(MainMenu, "loop")
def test_handle_ui(keypad_poll_mock, handle_key_mock, loop_mock):
    """
    The function to test function calls of the handle_ui function
    """
    tank_controller = TankController()

    tank_controller.handle_ui()
    keypad_poll_mock.assert_called()
    handle_key_mock.assert_called()
    loop_mock.assert_called()
