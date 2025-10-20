"""
The file to test the PumpVolume class
"""

from unittest import mock
from unittest.mock import ANY

from tank_controller.devices.library import LiquidCrystal
from tank_controller.tank_controller import TankController
from tank_controller.ui_state.main_menu import MainMenu
from tank_controller.ui_state.update_settings.update_settings import (
    UpdateSettings,
)
from tank_controller.ui_state.user_value.pump_volume import PumpVolume


@mock.patch.object(PumpVolume, "_set_next_state")
def test_handle_key(set_next_state_mock):
    """
    The function to test PumpVolume's handle_key function for each keypad input
    """
    pump_volume = PumpVolume(
        TankController(), UpdateSettings(TankController(), MainMenu(TankController()))
    )

    pump_volume.handle_key("A")
    set_next_state_mock.assert_not_called()

    pump_volume.value = "1"
    pump_volume.handle_key("A")
    set_next_state_mock.assert_called_with(ANY, True)
    assert set_next_state_mock.call_args.args[0].name() == "UpdateSettings"

    pump_volume.handle_key("C")
    assert pump_volume.value == ""

    pump_volume.handle_key("1")
    assert pump_volume.value[-1] == "1"

    pump_volume.handle_key("*")
    assert pump_volume.value[-1] == "."


@mock.patch.object(LiquidCrystal, "print")
def test_loop(print_mock):
    """
    The function to test PumpVolume's loop function's LiquidCrystal calls
    """
    pump_volume = PumpVolume(
        TankController(), UpdateSettings(TankController(), MainMenu(TankController()))
    )

    pump_volume.loop()
    print_mock.assert_has_calls(
        [
            mock.call("Volume in pump (ml):", line=1),
            mock.call("", style="center", line=2),
            mock.call("*=. A)ccept B)ack", line=3, style="center"),
            mock.call("D)ecline  C)lear", line=4, style="center"),
        ]
    )


@mock.patch.object(PumpVolume, "_set_next_state")
@mock.patch.object(LiquidCrystal, "print")
def test_pump_volume(print_mock, set_next_state_mock):
    """
    The function to test a use case of the PumpVolume class:
        User enters "3"
        User enters "."
        User enters "."
        User enters "1"
        User backspaces
        User backspaces
        User clears
        User accepts
    """
    pump_volume = PumpVolume(
        TankController(), UpdateSettings(TankController(), MainMenu(TankController()))
    )

    pump_volume.loop()
    print_mock.assert_has_calls(
        [
            mock.call("Volume in pump (ml):", line=1),
            mock.call("", style="center", line=2),
            mock.call("*=. A)ccept B)ack", line=3, style="center"),
            mock.call("D)ecline  C)lear", line=4, style="center"),
        ]
    )

    pump_volume.handle_key("3")
    assert pump_volume.value == "3"

    pump_volume.loop()
    print_mock.assert_has_calls(
        [
            mock.call("Volume in pump (ml):", line=1),
            mock.call("3", style="center", line=2),
            mock.call("*=. A)ccept B)ack", line=3, style="center"),
            mock.call("D)ecline  C)lear", line=4, style="center"),
        ]
    )

    pump_volume.handle_key("*")
    assert pump_volume.value == "3."

    pump_volume.loop()
    print_mock.assert_has_calls(
        [
            mock.call("Volume in pump (ml):", line=1),
            mock.call("3.", style="center", line=2),
            mock.call("*=. A)ccept B)ack", line=3, style="center"),
            mock.call("D)ecline  C)lear", line=4, style="center"),
        ]
    )

    pump_volume.handle_key("*")
    assert pump_volume.value == "3."

    pump_volume.loop()
    print_mock.assert_has_calls(
        [
            mock.call("Volume in pump (ml):", line=1),
            mock.call("3.", style="center", line=2),
            mock.call("*=. A)ccept B)ack", line=3, style="center"),
            mock.call("D)ecline  C)lear", line=4, style="center"),
        ]
    )

    pump_volume.handle_key("1")
    assert pump_volume.value == "3.1"

    pump_volume.loop()
    print_mock.assert_has_calls(
        [
            mock.call("Volume in pump (ml):", line=1),
            mock.call("3.1", style="center", line=2),
            mock.call("*=. A)ccept B)ack", line=3, style="center"),
            mock.call("D)ecline  C)lear", line=4, style="center"),
        ]
    )

    pump_volume.handle_key("B")
    assert pump_volume.value == "3."

    pump_volume.loop()
    print_mock.assert_has_calls(
        [
            mock.call("Volume in pump (ml):", line=1),
            mock.call("3.", style="center", line=2),
            mock.call("*=. A)ccept B)ack", line=3, style="center"),
            mock.call("D)ecline  C)lear", line=4, style="center"),
        ]
    )

    pump_volume.handle_key("B")
    assert pump_volume.value == "3"

    pump_volume.loop()
    print_mock.assert_has_calls(
        [
            mock.call("Volume in pump (ml):", line=1),
            mock.call("3", style="center", line=2),
            mock.call("*=. A)ccept B)ack", line=3, style="center"),
            mock.call("D)ecline  C)lear", line=4, style="center"),
        ]
    )

    pump_volume.handle_key("C")
    assert pump_volume.value == ""

    pump_volume.loop()
    print_mock.assert_has_calls(
        [
            mock.call("Volume in pump (ml):", line=1),
            mock.call("", style="center", line=2),
            mock.call("*=. A)ccept B)ack", line=3, style="center"),
            mock.call("D)ecline  C)lear", line=4, style="center"),
        ]
    )

    pump_volume.handle_key("A")
    set_next_state_mock.assert_not_called()
    assert pump_volume.value == ""

    pump_volume.loop()
    print_mock.assert_has_calls(
        [
            mock.call("Volume in pump (ml):", line=1),
            mock.call("", style="center", line=2),
            mock.call("*=. A)ccept B)ack", line=3, style="center"),
            mock.call("D)ecline  C)lear", line=4, style="center"),
        ]
    )

    pump_volume.handle_key("1")
    assert pump_volume.value == "1"

    pump_volume.loop()
    print_mock.assert_has_calls(
        [
            mock.call("Volume in pump (ml):", line=1),
            mock.call("1", style="center", line=2),
            mock.call("*=. A)ccept B)ack", line=3, style="center"),
            mock.call("D)ecline  C)lear", line=4, style="center"),
        ]
    )

    pump_volume.handle_key("A")
    set_next_state_mock.assert_called_with(ANY, True)
    assert set_next_state_mock.call_args.args[0].name() == "UpdateSettings"
    assert pump_volume.tank_controller.pump_volume == 1.0
