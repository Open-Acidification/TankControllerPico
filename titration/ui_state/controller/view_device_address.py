"""
The file to hold the View Device Address class
"""

from titration.devices.ethernet import Ethernet
from titration.devices.library import Keypad
from titration.ui_state.ui_state import UIState


class ViewDeviceAddress(UIState):
    """
    This is a class for the ViewDeviceAddress state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        Display the current IP and MAC address on the LCD.
        """
        ethernet = Ethernet()
        ip_str = ethernet.get_ip()
        mac_str = ethernet.get_mac()

        self.titrator.lcd.print(ip_str, line=1)
        self.titrator.lcd.print(mac_str, line=2)

    def handle_key(self, key):
        """
        Handle key presses for the ViewDeviceAddress state.
        """
        if key in (Keypad.KEY_4, Keypad.KEY_D):
            self._set_next_state(self.previous_state, True)
