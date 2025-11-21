"""
The file to test the MainMenu class
"""

from unittest import mock
from unittest.mock import ANY

from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.main_menu import MainMenu


@mock.patch.object(MainMenu, "_set_next_state")
def test_shortcuts(set_next_state_mock):
    """
    The function to test MainMenu's handle_key function for each keypad input
    """
    main_menu = MainMenu(Titrator())

    main_menu.handle_key("A")
    set_next_state_mock.assert_called_with(ANY, True)
    assert set_next_state_mock.call_args.args[0].name() == "SetPHTarget"

    main_menu.handle_key("B")
    set_next_state_mock.assert_called_with(ANY, True)
    assert set_next_state_mock.call_args.args[0].name() == "SetThermalTarget"


def test_handle_key_d():
    """
    The function to test MainMenu's handle_key function for each keypad input
    """
    main_menu = MainMenu(Titrator())

    main_menu.level1 = 2
    main_menu.level2 = 5
    main_menu.handle_key("D")
    assert main_menu.level1 == 0
    assert main_menu.level2 == -1


def test_handle_up():
    """
    The function to test MainMenu's handle_key function for each keypad input
    """
    main_menu = MainMenu(Titrator())
    main_menu.level1 = 0
    main_menu.level2 = -1
    main_menu.handle_key("2")
    assert main_menu.level1 == 2
    assert main_menu.level2 == -1

    main_menu.level1 = 1
    main_menu.level2 = 0
    main_menu.handle_key("2")
    assert main_menu.level2 == main_menu.view_command_count - 1

    main_menu.level1 = 2
    main_menu.level2 = 0
    main_menu.handle_key("2")
    assert main_menu.level2 == main_menu.set_command_count - 1


def test_handle_left():
    """
    The function to test MainMenu's handle_key function for each keypad input
    """
    main_menu = MainMenu(Titrator())

    main_menu.level1 = 1
    main_menu.level2 = -1
    main_menu.handle_key("4")
    assert main_menu.level1 == 0
    assert main_menu.level2 == -1

    main_menu.level1 = 1
    main_menu.level2 = 0
    main_menu.handle_key("4")
    assert main_menu.level1 == 1
    assert main_menu.level2 == -1

    main_menu.level1 = 2
    main_menu.level2 = 0
    main_menu.handle_key("4")
    assert main_menu.level1 == 2
    assert main_menu.level2 == -1


@mock.patch.object(MainMenu, "_set_next_state")
def test_handle_right(set_next_state_mock):
    """
    The function to test MainMenu's handle_key function for each keypad input
    """
    main_menu = MainMenu(Titrator())
    main_menu.level1 = 0
    main_menu.level2 = -1
    main_menu.handle_key("6")
    assert main_menu.level1 == 1
    assert main_menu.level2 == -1

    main_menu.level1 = 1
    main_menu.level2 = -1
    main_menu.handle_key("6")
    assert main_menu.level2 == 0

    main_menu.level1 = 1
    main_menu.level2 = 0
    main_menu.handle_key("6")
    set_next_state_mock.assert_called_with(ANY, True)
    assert main_menu.level1 == 1

    main_menu.level1 = 2
    main_menu.level2 = 0
    main_menu.handle_key("6")
    set_next_state_mock.assert_called_with(ANY, True)
    assert main_menu.level1 == 2


def test_handle_down():
    """
    The function to test MainMenu's handle_key function for each keypad input
    """
    main_menu = MainMenu(Titrator())
    main_menu.level1 = 0
    main_menu.level2 = -1
    main_menu.handle_key("8")
    assert main_menu.level1 == 1
    assert main_menu.level2 == -1

    main_menu.level1 = 1
    main_menu.level2 = 0
    main_menu.handle_key("8")
    assert main_menu.level2 == 1

    main_menu.level1 = 2
    main_menu.level2 = 0
    main_menu.handle_key("8")
    assert main_menu.level2 == 1


@mock.patch.object(LiquidCrystal, "print")
def test_view_list(print_mock):
    """
    The function to test navigation to submenu view features
    """
    main_menu = MainMenu(Titrator())

    main_menu.loop()
    print_mock.assert_any_call("Idle Line 1", line=1)
    print_mock.assert_any_call("Idle Line 2", line=2)
    print_mock.reset_mock()

    main_menu.handle_key("6")
    main_menu.loop()
    print_mock.assert_any_call("View settings", line=1)
    print_mock.assert_any_call("<4   ^2  8v   6>", line=2)
    print_mock.reset_mock()

    main_menu.handle_key("6")
    for index, label in enumerate(main_menu.view_menus):
        print_mock.reset_mock()
        if index != 0:
            main_menu.handle_key("8")
        main_menu.loop()
        print_mock.assert_any_call(label, line=1)


@mock.patch.object(LiquidCrystal, "print")
def test_change_list(print_mock):
    """
    The function to test navigation to submenu set features
    """
    main_menu = MainMenu(Titrator())

    main_menu.loop()
    print_mock.assert_any_call("Idle Line 1", line=1)
    print_mock.assert_any_call("Idle Line 2", line=2)
    print_mock.reset_mock()

    main_menu.handle_key("6")
    main_menu.handle_key("8")
    main_menu.loop()
    print_mock.assert_any_call("Change settings", line=1)
    print_mock.assert_any_call("<4   ^2  8v   6>", line=2)
    print_mock.reset_mock()

    main_menu.handle_key("6")
    for index, label in enumerate(main_menu.set_menus):
        print_mock.reset_mock()
        if index != 0:
            main_menu.handle_key("8")
        main_menu.loop()
        print_mock.assert_any_call(label, line=1)
