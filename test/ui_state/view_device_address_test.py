"""
The file to test the View Google Minutes class
"""

from unittest import mock

from titration.devices.library import LiquidCrystal
from titration.titrator import Titrator
from titration.ui_state.controller.view_device_address import (
    ViewDeviceAddress,
)
from titration.ui_state.main_menu import MainMenu
from titration.ui_state.ui_state import UIState
from titration.devices.ethernet import EthernetTC


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """
    def __init__(self, titrator):
        super().__init__(titrator)


def test_view_device_address_gets_ip():
    """Assert the IP is printed on line 1 (deterministic).

    Patch `EthernetTC.get_ip` so the test doesn't depend on the host
    network configuration.
    """
    with mock.patch.object(LiquidCrystal, "print") as print_mock:
        with mock.patch.object(EthernetTC, "get_ip", return_value="192.168.1.10"):
            state = ViewDeviceAddress(Titrator(), MainMenu(Titrator()))
            state.loop()

            print_mock.assert_any_call("192.168.1.10", line=1)


def test_view_device_address_gets_mac_with_uuid():
    """
    Assert the MAC is printed on line 2 (deterministic).
    """
    with mock.patch.object(LiquidCrystal, "print") as print_mock:
        with mock.patch.object(EthernetTC, "get_mac", return_value="6C0B:5E18:15FB"):
            state = ViewDeviceAddress(Titrator(), MainMenu(Titrator()))
            state.loop()

            print_mock.assert_any_call("6C0B:5E18:15FB", line=2)


@mock.patch.object(LiquidCrystal, "print")
def test_handle_key_hash(print_mock):
    """Pressing KEY_HASH should print 'WDT disabled' on line 1."""
    titrator = Titrator()
    titrator.state = ViewDeviceAddress(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("#")

    print_mock.assert_any_call("WDT disabled", line=1)


@mock.patch.object(LiquidCrystal, "print")
def test_handle_key_b(print_mock):
    """Pressing KEY_B should print 'WDT test' on line 1."""
    titrator = Titrator()
    titrator.state = ViewDeviceAddress(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("B")

    print_mock.assert_any_call("WDT test", line=1)


@mock.patch.object(LiquidCrystal, "print")
def test_handle_key_c_reads_mac_and_prints(print_mock):
    """Pressing KEY_C should call EthernetTC.read_mac, print the returned
    string on line 2"""
    titrator = Titrator()
    state = ViewDeviceAddress(titrator, MockPreviousState(titrator))

    mac_str = "90A2:DA12:3456"

    with mock.patch.object(EthernetTC, "read_mac", return_value=mac_str):
        state.handle_key("C")

    # It should have printed the MAC returned by read_mac on line 2
    print_mock.assert_any_call(mac_str, line=2)


def test_handle_key_4():
    """
    The function to test the back handle key
    """
    titrator = Titrator()

    titrator.state = ViewDeviceAddress(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("4")
    assert isinstance(titrator.state, MockPreviousState)


def test_handle_key_d():
    """
    The function to test the reset handle keys
    """
    titrator = Titrator()

    titrator.state = ViewDeviceAddress(titrator, MockPreviousState(titrator))

    titrator.state.handle_key("D")
    assert isinstance(titrator.state, MockPreviousState)
