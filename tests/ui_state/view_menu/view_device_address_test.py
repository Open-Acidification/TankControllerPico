"""
The file to test the View Google Minutes class
"""

from unittest import mock

from src.devices.ethernet import Ethernet
from src.devices.library import LiquidCrystal
from src.titrator import Titrator
from src.ui_state.ui_state import UIState
from src.ui_state.view_menu.view_device_address import ViewDeviceAddress


class MockPreviousState(UIState):
    """
    A mock previous state for testing purposes
    """

    def __init__(self, titrator):
        super().__init__(titrator)


def test_view_device_address():
    """
    The function to test the view device address loop for correct IP and MAC display
    """
    with mock.patch.object(LiquidCrystal, "print") as print_mock:
        with mock.patch.object(Ethernet, "get_ip", return_value="192.168.1.10"):
            with mock.patch.object(Ethernet, "get_mac", return_value="90A2:DA00:0000"):
                state = ViewDeviceAddress(Titrator(), MockPreviousState(Titrator()))
                state.loop()

                print_mock.assert_any_call("192.168.1.10", line=1)
                print_mock.assert_any_call("90A2:DA00:0000", line=2)


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
