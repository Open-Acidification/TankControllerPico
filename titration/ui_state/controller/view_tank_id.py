"""
The file to hold the View Tank ID class
"""

from titration.devices.library import Keypad
from titration.ui_state.ui_state import UIState


class ViewTankID(UIState):
    """
    This is a class for the ViewTankID state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        The constructor for the ViewTankID class
        """
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        The loop function for the ViewTankID class
        """
        self.titrator.lcd.print("Tank ID:", line=1)
        self.titrator.lcd.print(f"{self.titrator.eeprom.get_tank_id(0)}", line=2)

    def handle_key(self, key):
        """
        The handle_key function for the ViewTankID class
        """
        if key in [Keypad.KEY_4, Keypad.KEY_D]:
            self._set_next_state(self.previous_state, True)
