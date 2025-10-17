"""
The file to test the MainMenu class
"""

from unittest import mock
from unittest.mock import ANY

from titration.devices.library import LiquidCrystal
from titration.titrator import Titrator
from titration.ui_state.main_menu import MainMenu


@mock.patch.object(MainMenu, "_set_next_state")
def test_handle_key(set_next_state_mock):
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

    main_menu.level1 = 2
    main_menu.level2 = 5
    main_menu.handle_key("D")
    assert main_menu.level1 == 0
    assert main_menu.level2 == -1

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
def test_loop(print_mock):
    """
    The function to test MainMenu's loop function's LiquidCrystal calls
    """
    main_menu = MainMenu(Titrator())

    main_menu.loop()
    print_mock.assert_any_call("Idle Line 1", line=1)
    print_mock.assert_any_call("Idle Line 2", line=2)

    print_mock.reset_mock()

    main_menu.level1 = 1
    main_menu.level2 = -1
    main_menu.loop()
    print_mock.assert_has_calls(
        [mock.call("View settings", line=1), mock.call("<4   ^2  8v   6>", line=2)]
    )

    print_mock.reset_mock()

    main_menu.level1 = 1
    main_menu.level2 = 2
    main_menu.loop()
    print_mock.assert_has_calls(
        [
            mock.call(main_menu.view_menus[2], line=1),
            mock.call("<4   ^2  8v   6>", line=2),
        ]
    )

    print_mock.reset_mock()

    main_menu.level1 = 2
    main_menu.level2 = -1
    main_menu.loop()
    print_mock.assert_has_calls(
        [mock.call("Change settings", line=1), mock.call("<4   ^2  8v   6>", line=2)]
    )

    print_mock.reset_mock()

    main_menu.level1 = 2
    main_menu.level2 = 3
    main_menu.loop()
    print_mock.assert_has_calls(
        [
            mock.call(main_menu.set_menus[3], line=1),
            mock.call("<4   ^2  8v   6>", line=2),
        ]
    )
